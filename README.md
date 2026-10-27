# PrepTrack – Personalized Learning and Performance Analysis Platform

PrepTrack is a web-based personalized learning platform designed to help users improve their learning performance through quiz assessments and performance analysis. Instead of requiring users to identify their weaknesses manually, the application evaluates their quiz performance to help identify topics that need improvement and guide them toward focused practice.

Built using Python, Flask, SQLite, HTML, CSS, and JavaScript, PrepTrack combines quiz assessments, performance tracking, practice session management, and detailed answer reviews in one platform.

## Project Objective

PrepTrack aims to make learning more focused and effective by using quiz performance to identify areas for improvement and guide users toward relevant practice. By combining assessment, performance analysis, focused quizzes, and historical tracking, the platform encourages a more structured and personalized learning experience.

## Key Features

### 1. User Authentication
- User registration and login.
- Password confirmation during registration.
- Session-based user authentication.
- Access to personalized learning activities.

### 2. Performance-Based Weakness Identification
- Evaluate quiz performance using assessment results.
- Analyze scores and accuracy to help identify topics that require additional practice.
- Use performance information to guide users toward areas needing improvement.
- Support a more focused learning process instead of relying entirely on manual self-assessment.

### 3. Focused Quiz Recommendations
- Recommend quizzes based on identified learning gaps.
- Help users concentrate on topics where their performance indicates a need for improvement.
- Encourage targeted practice and continuous learning.

### 4. Quiz Assessment
- Access available quizzes through the quiz interface.
- Answer topic-based questions and submit responses.
- Evaluate submitted answers and calculate quiz results.
- Review correct answers and explanations when available.

### 5. Interactive Quiz Results
- Display quiz scores, accuracy, and time taken.
- Compare user responses with correct answers.
- Review explanations for individual questions when available.
- Search and filter questions on the results page.
- Expand or collapse question details.
- Print quiz results for later reference.

### 6. Practice Session Management
- Record study and practice sessions.
- Access previously recorded practice activities.
- Organize learning activities through the practice history interface.

### 7. Quiz History and Performance Tracking
- Access previous quiz attempts.
- Review saved quiz results and answer details when available.
- Use historical performance information to reflect on learning progress.

### 8. Database Management
- Use SQLite for persistent data storage.
- Integrate database operations through Flask-SQLAlchemy.
- Organize application data using database models and tables.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend application logic and performance evaluation |
| Flask | Web framework and request routing |
| Flask-SQLAlchemy | Database integration and ORM |
| SQLite | Persistent application data storage |
| HTML5 | Web page structure |
| CSS3 | Styling and responsive presentation |
| JavaScript | Client-side interactivity |
| Jinja2 | Dynamic HTML rendering |
| Git and GitHub | Version control and source code hosting |

---

## Project Structure

```text
PrepTrack/
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── dashboard.js
│       └── quiz.js
│
├── templates/
│   ├── add_session.html
│   ├── base.html
│   ├── history.html
│   ├── index.html
│   ├── login.html
│   ├── quiz_history.html
│   ├── quiz_result.html
│   ├── quizzes.html
│   ├── register.html
│   └── take_quiz.html
│
├── app.py
├── database.py
├── quiz_data.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Main Files and Their Responsibilities

- **`app.py`** – Main Flask application, routing, request handling, authentication, and application logic.
- **`database.py`** – Database-related functionality and integration.
- **`quiz_data.py`** – Quiz questions and associated quiz data.
- **`templates/base.html`** – Shared layout for application pages.
- **`templates/index.html`** – Main landing or dashboard page, depending on the configured route.
- **`templates/login.html`** – User login interface.
- **`templates/register.html`** – User registration interface.
- **`templates/add_session.html`** – Practice session entry form.
- **`templates/history.html`** – Practice session history.
- **`templates/quizzes.html`** – Quiz browsing and selection interface.
- **`templates/take_quiz.html`** – Quiz-taking interface.
- **`templates/quiz_result.html`** – Quiz results, answer reviews, and interactive result controls.
- **`templates/quiz_history.html`** – Previous quiz attempts.
- **`static/css/style.css`** – Application styling.
- **`static/js/dashboard.js`** – Dashboard-related JavaScript.
- **`static/js/quiz.js`** – Quiz-related client-side JavaScript.
- **`requirements.txt`** – Python package dependencies.
- **`.gitignore`** – Files and directories excluded from Git tracking.

---

## How PrepTrack Works

PrepTrack follows a performance-driven learning workflow.

### Step 1: User Registration and Login
Users create an account and log in to access the application's learning features.

### Step 2: Quiz Assessment
Users attempt available quizzes and submit their answers. The application evaluates their responses and generates assessment results.

### Step 3: Performance Evaluation
The application uses quiz results, including scores and accuracy, to evaluate performance. This information helps identify topics where the user may need additional practice.

### Step 4: Weak Topic Identification
Based on the implemented performance evaluation logic, the application identifies learning areas that require more attention rather than depending entirely on users to identify those areas themselves.

### Step 5: Focused Quiz Recommendations
The application guides users toward quizzes focused on identified weak topics, helping them spend more time practising areas where improvement is needed.

### Step 6: Results and Answer Review
After completing a quiz, users can view their scores, accuracy, time taken, and answer reviews. Interactive search and filtering controls make it easier to inspect individual questions.

### Step 7: History and Continued Improvement
Users can revisit previous quiz attempts and recorded practice sessions. Historical results provide information that can help them monitor their learning and focus future practice.

---

## Getting Started

Follow these instructions to run PrepTrack locally.

### Prerequisites

- Python installed on your system.
- pip, the Python package installer.
- Git, if cloning the repository.

### 1. Clone the Repository

Replace the placeholder with your actual GitHub repository URL.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd PrepTrack
```

Alternatively, download the repository ZIP file and extract it.

### 2. Create a Virtual Environment

On Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure `requirements.txt` includes all third-party packages imported by the application.

### 4. Configure the Flask Secret Key

PrepTrack requires a secret key supplied through the `SECRET_KEY` environment variable.

Generate a secure key:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

In Windows Command Prompt, set the generated value:

```cmd
set SECRET_KEY=YOUR_GENERATED_SECRET_KEY
```

Replace the placeholder with your generated key.

Keep this key private. Do not commit it to GitHub.

### 5. Run the Application

```bash
python app.py
```

Open the local address displayed in the terminal. With the default Flask development settings, this is usually:

```text
http://127.0.0.1:5000/
```

### 6. Explore the Application

1. Register an account.
2. Log in.
3. Explore the dashboard and practice session features.
4. Attempt an available quiz.
5. Review your assessment results.
6. Explore performance-based recommendations, where implemented.
7. Visit the history pages to review previous activities.

---

## Security Considerations

- Store secret keys in environment variables rather than hardcoding them.
- Do not commit credentials or sensitive environment files.
- Keep virtual environments and unnecessary local database files out of version control.
- Use secure password-handling practices.
- Disable debug mode and use a production-ready server when deploying the application.

---

## Future Enhancements

Potential future improvements include:

- Visual dashboards for topic-wise performance.
- Progress charts across repeated quiz attempts.
- Personalized study plans based on performance trends.
- Difficulty-based quiz recommendations.
- Learning goals and progress summaries.
- Additional analytics to help users understand improvement over time.

These are possible future enhancements and are not claims about existing functionality.

---

