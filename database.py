from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

    practice_sessions = db.relationship(
        "PracticeSession",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )

    quiz_attempts = db.relationship(
        "QuizAttempt",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )


class PracticeSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=True,
        index=True
    )
    subject = db.Column(db.String(50), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    questions_attempted = db.Column(db.Integer, nullable=False)
    correct_answers = db.Column(db.Integer, nullable=False)
    time_spent = db.Column(db.Integer, nullable=False)  # minutes
    practice_date = db.Column(db.Date, nullable=False)


class QuizAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=True,
        index=True
    )
    subject = db.Column(db.String(50), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    accuracy = db.Column(db.Float, nullable=False)
    time_taken = db.Column(db.Integer, nullable=False)  # seconds
    review_json = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, default=datetime.now, nullable=False)