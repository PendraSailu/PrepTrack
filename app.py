import json
import os
from datetime import date, datetime
from functools import wraps
from time import time

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)
from sqlalchemy import func, inspect, text
from werkzeug.security import generate_password_hash, check_password_hash

from database import db, User, PracticeSession, QuizAttempt
from quiz_data import QUIZ_DATA


app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if not app.config["SECRET_KEY"]:
    raise RuntimeError("Please set the SECRET_KEY environment variable.")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///preptrack.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

QUIZ_DURATION = 300  # Five minutes per quiz

SUBJECTS = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "Data Structures & Algorithms",
    "Object-Oriented Programming",
    "DBMS",
    "Operating Systems",
    "Computer Networks",
    "Software Engineering",
    "HTML",
    "CSS",
    "React",
    "SQL",
    "Aptitude",
    "Verbal Ability",
    "Logical Reasoning"
]


def login_required(view_function):
    """Require a signed-in user before opening a private page."""
    @wraps(view_function)
    def wrapped_view(*args, **kwargs):
        user_id = session.get("user_id")
        if not user_id or db.session.get(User, user_id) is None:
            session.pop("user_id", None)
            flash("Please log in to continue.", "error")
            return redirect(url_for("login"))
        return view_function(*args, **kwargs)
    return wrapped_view


@app.context_processor
def inject_logged_in_user():
    user = None
    user_id = session.get("user_id")
    if user_id:
        user = db.session.get(User, user_id)
    return {"logged_in_user": user}


def current_user_id():
    return session["user_id"]


def get_topic_status(accuracy, attempts):
    """Return a status and recommendation based on performance."""
    if attempts < 5:
        return (
            "More data needed",
            "Attempt at least 5 questions before judging this topic."
        )

    if accuracy < 50:
        return (
            "High priority",
            "Revise the basics, then solve 10 easy questions."
        )

    if accuracy < 70:
        return (
            "Needs practice",
            "Review mistakes and solve 10–15 more questions."
        )

    if accuracy < 85:
        return (
            "Good",
            "Practice a few medium-level questions to improve further."
        )

    return (
        "Strong",
        "Revise periodically and try harder questions."
    )


# --------------------------------------------------
# LOGIN / REGISTRATION
# --------------------------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("user_id"):
        return redirect(url_for("index"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not name or not email or not password:
            flash("Please fill in all required fields.", "error")
            return render_template("register.html")

        if len(name) > 100:
            flash("Name must be 100 characters or fewer.", "error")
            return render_template("register.html")

        if "@" not in email or len(email) > 120:
            flash("Please enter a valid email address.", "error")
            return render_template("register.html")

        if len(password) < 8:
            flash("Password must contain at least 8 characters.", "error")
            return render_template("register.html")

        if not confirm_password or password != confirm_password:
            flash("Passwords do not match.", "error")
            return render_template("register.html")

        if User.query.filter(func.lower(User.email) == email).first():
            flash("An account with this email already exists.", "error")
            return render_template("register.html")

        # If this is the first account, associate any legacy records
        # with it so existing practice and quiz history is preserved.
        is_first_user = User.query.count() == 0

        user = User(
            name=name,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()

        if is_first_user:
            PracticeSession.query.filter(
                PracticeSession.user_id.is_(None)
            ).update(
                {PracticeSession.user_id: user.id},
                synchronize_session=False
            )
            QuizAttempt.query.filter(
                QuizAttempt.user_id.is_(None)
            ).update(
                {QuizAttempt.user_id: user.id},
                synchronize_session=False
            )
            db.session.commit()

        session.clear()
        session["user_id"] = user.id
        flash("Your account was created successfully.", "success")
        return redirect(url_for("index"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user_id"):
        user = db.session.get(User, session["user_id"])
        if user:
            return redirect(url_for("index"))
        session.pop("user_id", None)

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = User.query.filter(func.lower(User.email) == email).first()

        if user is None or not check_password_hash(user.password_hash, password):
            flash("Invalid email or password.", "error")
            return render_template("login.html")

        session.clear()
        session["user_id"] = user.id
        flash(f"Welcome back, {user.name}!", "success")
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

@app.route("/")
@login_required
def index():
    user_id = current_user_id()

    sessions = PracticeSession.query.filter_by(
        user_id=user_id
    ).order_by(
        PracticeSession.practice_date.desc(),
        PracticeSession.id.desc()
    ).all()

    total_attempted = sum(s.questions_attempted for s in sessions)
    total_correct = sum(s.correct_answers for s in sessions)
    total_minutes = sum(s.time_spent for s in sessions)

    overall_accuracy = (
        round((total_correct / total_attempted) * 100, 1)
        if total_attempted else 0
    )

    topics_count = len({
        (s.subject, s.topic.strip().lower())
        for s in sessions
    })

    subject_rows = db.session.query(
        PracticeSession.subject,
        func.sum(PracticeSession.questions_attempted).label("attempted"),
        func.sum(PracticeSession.correct_answers).label("correct")
    ).filter(
        PracticeSession.user_id == user_id
    ).group_by(
        PracticeSession.subject
    ).all()

    subject_labels = [row.subject for row in subject_rows]
    subject_accuracies = [
        round((row.correct / row.attempted) * 100, 1)
        if row.attempted else 0
        for row in subject_rows
    ]

    topic_rows = db.session.query(
        PracticeSession.subject,
        PracticeSession.topic,
        func.sum(PracticeSession.questions_attempted).label("attempted"),
        func.sum(PracticeSession.correct_answers).label("correct")
    ).filter(
        PracticeSession.user_id == user_id
    ).group_by(
        PracticeSession.subject,
        PracticeSession.topic
    ).all()

    topic_summaries = []
    for row in topic_rows:
        accuracy = (
            round((row.correct / row.attempted) * 100, 1)
            if row.attempted else 0
        )
        status, recommendation = get_topic_status(accuracy, row.attempted)
        topic_summaries.append({
            "subject": row.subject,
            "topic": row.topic,
            "attempted": row.attempted,
            "correct": row.correct,
            "accuracy": accuracy,
            "status": status,
            "recommendation": recommendation
        })

    priority_order = {
        "High priority": 0,
        "Needs practice": 1,
        "More data needed": 2,
        "Good": 3,
        "Strong": 4
    }
    topic_summaries.sort(
        key=lambda item: (
            priority_order[item["status"]],
            item["accuracy"]
        )
    )

    return render_template(
        "index.html",
        total_attempted=total_attempted,
        overall_accuracy=overall_accuracy,
        total_minutes=total_minutes,
        topics_count=topics_count,
        subject_labels=subject_labels,
        subject_accuracies=subject_accuracies,
        topic_summaries=topic_summaries[:6],
        recent_sessions=sessions[:5]
    )


# --------------------------------------------------
# MANUAL PRACTICE SESSIONS
# --------------------------------------------------

@app.route("/add", methods=["GET", "POST"])
@login_required
def add_session():
    if request.method == "POST":
        subject = request.form.get("subject", "").strip()
        topic = request.form.get("topic", "").strip()
        attempted_text = request.form.get("questions_attempted", "").strip()
        correct_text = request.form.get("correct_answers", "").strip()
        time_text = request.form.get("time_spent", "").strip()
        date_text = request.form.get("practice_date", "").strip()

        if subject not in SUBJECTS:
            flash("Please select a valid subject.", "error")
            return render_template(
                "add_session.html",
                subjects=SUBJECTS,
                today=date.today().isoformat()
            )

        if not topic:
            flash("Please enter a topic.", "error")
            return render_template(
                "add_session.html",
                subjects=SUBJECTS,
                today=date.today().isoformat()
            )

        try:
            attempted = int(attempted_text)
            correct = int(correct_text)
            minutes = int(time_text)
            practice_date = date.fromisoformat(date_text)
        except (ValueError, TypeError):
            flash("Enter valid whole numbers and a valid date.", "error")
            return render_template(
                "add_session.html",
                subjects=SUBJECTS,
                today=date.today().isoformat()
            )

        if attempted <= 0:
            flash("Questions attempted must be at least 1.", "error")
            return render_template(
                "add_session.html",
                subjects=SUBJECTS,
                today=date.today().isoformat()
            )

        if correct < 0 or correct > attempted:
            flash(
                "Correct answers must be between 0 and questions attempted.",
                "error"
            )
            return render_template(
                "add_session.html",
                subjects=SUBJECTS,
                today=date.today().isoformat()
            )

        if minutes < 0:
            flash("Time spent cannot be negative.", "error")
            return render_template(
                "add_session.html",
                subjects=SUBJECTS,
                today=date.today().isoformat()
            )

        practice = PracticeSession(
            user_id=current_user_id(),
            subject=subject,
            topic=topic,
            questions_attempted=attempted,
            correct_answers=correct,
            time_spent=minutes,
            practice_date=practice_date
        )
        db.session.add(practice)
        db.session.commit()

        flash("Practice session saved successfully.", "success")
        return redirect(url_for("index"))

    return render_template(
        "add_session.html",
        subjects=SUBJECTS,
        today=date.today().isoformat()
    )


@app.route("/history")
@login_required
def history():
    sessions = PracticeSession.query.filter_by(
        user_id=current_user_id()
    ).order_by(
        PracticeSession.practice_date.desc(),
        PracticeSession.id.desc()
    ).all()
    return render_template("history.html", sessions=sessions)


@app.route("/delete/<int:session_id>", methods=["POST"])
@login_required
def delete_session(session_id):
    practice = PracticeSession.query.filter_by(
        id=session_id,
        user_id=current_user_id()
    ).first_or_404()

    db.session.delete(practice)
    db.session.commit()
    flash("Practice session deleted.", "success")
    return redirect(url_for("history"))


# --------------------------------------------------
# PRACTICE SHEETS / QUIZZES
# --------------------------------------------------

@app.route("/quizzes")
@login_required
def quizzes():
    return render_template("quizzes.html", quiz_data=QUIZ_DATA)


@app.route("/take-quiz")
@login_required
def take_quiz():
    subject = request.args.get("subject", "")
    topic = request.args.get("topic", "")

    if subject not in QUIZ_DATA:
        flash("Please select a valid subject.", "error")
        return redirect(url_for("quizzes"))

    if topic not in QUIZ_DATA[subject]:
        flash("Please select a valid topic.", "error")
        return redirect(url_for("quizzes"))

    questions = QUIZ_DATA[subject][topic]
    if not questions:
        flash("No questions are available for this topic.", "error")
        return redirect(url_for("quizzes"))

    quiz_key = f"{subject}::{topic}"
    session["active_quiz"] = {
        "key": quiz_key,
        "started_at": time()
    }

    return render_template(
        "take_quiz.html",
        subject=subject,
        topic=topic,
        questions=questions,
        duration=QUIZ_DURATION
    )


@app.route("/submit-quiz", methods=["POST"])
@login_required
def submit_quiz():
    subject = request.form.get("subject", "")
    topic = request.form.get("topic", "")

    if subject not in QUIZ_DATA:
        flash("Invalid quiz subject.", "error")
        return redirect(url_for("quizzes"))

    if topic not in QUIZ_DATA[subject]:
        flash("Invalid quiz topic.", "error")
        return redirect(url_for("quizzes"))

    active_quiz = session.get("active_quiz")
    quiz_key = f"{subject}::{topic}"
    if not active_quiz or active_quiz.get("key") != quiz_key:
        flash("Please start the quiz before submitting.", "error")
        return redirect(url_for("quizzes"))

    started_at = active_quiz.get("started_at")
    if not isinstance(started_at, (int, float)):
        session.pop("active_quiz", None)
        flash("Quiz session is invalid. Please start again.", "error")
        return redirect(url_for("quizzes"))

    elapsed = max(0, int(time() - started_at))
    timed_out = elapsed > QUIZ_DURATION
    questions = QUIZ_DATA[subject][topic]
    review = []
    score = 0

    for index, question in enumerate(questions):
        selected_text = request.form.get(f"q{index}", "")
        try:
            selected_index = int(selected_text)
        except (ValueError, TypeError):
            selected_index = -1

        if selected_index < 0 or selected_index >= len(question["options"]):
            selected_index = -1

        correct_index = question["answer"]
        if timed_out:
            selected_index = -1

        is_correct = selected_index == correct_index
        if is_correct:
            score += 1

        user_answer = (
            question["options"][selected_index]
            if selected_index >= 0
            else "Not answered"
        )

        review.append({
            "question": question["question"],
            "user_answer": user_answer,
            "correct_answer": question["options"][correct_index],
            "is_correct": is_correct,
            "explanation": question.get("explanation", ""),
            "selected_index": selected_index,
            "correct_index": correct_index
        })

    total = len(questions)
    accuracy = round((score / total) * 100, 1) if total else 0
    time_taken = min(elapsed, QUIZ_DURATION)
    minutes_spent = max(1, (time_taken + 59) // 60)

    attempt = QuizAttempt(
        user_id=current_user_id(),
        subject=subject,
        topic=topic,
        score=score,
        total=total,
        accuracy=accuracy,
        time_taken=time_taken,
        review_json=json.dumps(review)
    )
    db.session.add(attempt)

    practice = PracticeSession(
        user_id=current_user_id(),
        subject=subject,
        topic=topic,
        questions_attempted=total,
        correct_answers=score,
        time_spent=minutes_spent,
        practice_date=date.today()
    )
    db.session.add(practice)
    db.session.commit()
    session.pop("active_quiz", None)

    return render_template(
        "quiz_result.html",
        subject=subject,
        topic=topic,
        score=score,
        total=total,
        accuracy=accuracy,
        time_taken=time_taken,
        review=review,
        timed_out=timed_out
    )


@app.route("/quiz-history")
@login_required
def quiz_history():
    attempts = QuizAttempt.query.filter_by(
        user_id=current_user_id()
    ).order_by(
        QuizAttempt.date.desc(),
        QuizAttempt.id.desc()
    ).all()
    return render_template("quiz_history.html", attempts=attempts)


@app.route("/quiz-result/<int:attempt_id>")
@login_required
def quiz_result(attempt_id):
    attempt = QuizAttempt.query.filter_by(
        id=attempt_id,
        user_id=current_user_id()
    ).first_or_404()

    review = []
    if attempt.review_json:
        try:
            review = json.loads(attempt.review_json)
        except (json.JSONDecodeError, TypeError):
            review = []

    # Older attempts did not store selected answers. For those records,
    # show the correct answer and explanation without inventing selections.
    if not review:
        questions = QUIZ_DATA.get(attempt.subject, {}).get(attempt.topic, [])
        for question in questions:
            review.append({
                "question": question["question"],
                "user_answer": "Not recorded for this older attempt",
                "correct_answer": question["options"][question["answer"]],
                "is_correct": False,
                "explanation": question.get("explanation", ""),
                "selected_index": -1,
                "correct_index": question["answer"]
            })

    return render_template(
        "quiz_result.html",
        subject=attempt.subject,
        topic=attempt.topic,
        score=attempt.score,
        total=attempt.total,
        accuracy=attempt.accuracy,
        time_taken=attempt.time_taken,
        review=review,
        timed_out=False
    )


# --------------------------------------------------
# DATABASE SETUP / SAFE SQLITE MIGRATION
# --------------------------------------------------

def migrate_existing_database():
    """Add new columns to an older SQLite database without deleting records."""
    inspector = inspect(db.engine)
    table_names = inspector.get_table_names()

    if "practice_session" in table_names:
        practice_columns = {
            column["name"]
            for column in inspector.get_columns("practice_session")
        }
        if "user_id" not in practice_columns:
            db.session.execute(
                text("ALTER TABLE practice_session ADD COLUMN user_id INTEGER")
            )

    if "quiz_attempt" in table_names:
        quiz_columns = {
            column["name"]
            for column in inspector.get_columns("quiz_attempt")
        }
        if "user_id" not in quiz_columns:
            db.session.execute(
                text("ALTER TABLE quiz_attempt ADD COLUMN user_id INTEGER")
            )
        if "review_json" not in quiz_columns:
            db.session.execute(
                text("ALTER TABLE quiz_attempt ADD COLUMN review_json TEXT")
            )

    db.session.commit()


with app.app_context():
    db.create_all()
    migrate_existing_database()


if __name__ == "__main__":
    app.run(debug=True)
