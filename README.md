# PrepTrack – Personal Study and Quiz Tracker

PrepTrack is a web-based study tracking application built with Flask and Python. It helps users organize their practice sessions, take quizzes, review their performance, and track their learning progress in one place.

The application provides a simple interface for managing study activities, attempting topic-based quizzes, reviewing answers, and accessing previous quiz results.

## 🎯 Project Objective

The objective of PrepTrack is to provide a convenient platform for managing study practice and quiz activities. By bringing practice session tracking, quizzes, answer reviews, and historical results together, the application helps users organize their learning and reflect on their performance.

## ✨ Features

### 🔐 User Authentication
- User registration and login.
- Password confirmation during registration.
- Session-based access to authenticated features.
- Logout functionality.

### 📊 Dashboard
- Access the application's main dashboard.
- Navigate to practice sessions, history, and quizzes.
- Use the dashboard as the central point for study activities.

### 📝 Practice Session Tracking
- Add and manage study practice sessions.
- Record study-related information.
- View previously recorded practice sessions.
- Track your study activities over time.

### 📚 Topic-Based Quizzes
- Access quizzes through the quizzes page.
- Attempt quizzes based on subjects and topics.
- Select answers and submit your responses.
- Receive results after submitting a quiz.

### 📈 Interactive Quiz Results
- View your quiz score and total questions.
- Check your accuracy percentage.
- See the time taken to complete the quiz.
- Review your answers alongside the correct answers.
- Read explanations when available.
- Search and filter questions on the results page.
- Expand or collapse question details.
- Print your quiz results.
- Navigate to another quiz or browse available quizzes.

### 🕘 History and Progress Review
- View recorded practice sessions.
- Access previous quiz attempts.
- Review saved quiz results and answers when available.

### 🗄️ Database Management
- Uses SQLite for local data storage.
- Uses Flask-SQLAlchemy to interact with the database.
- Stores application data in database tables.
- Supports database table creation through the application's database initialization process.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic and backend development |
| Flask | Web framework and routing |
| Flask-SQLAlchemy | Database integration and ORM |
| SQLite | Database storage |
| HTML5 | Web page structure |
| CSS3 | Styling and responsive layouts |
| JavaScript | Client-side interactivity |
| Jinja2 | Dynamic HTML templates |
| Git and GitHub | Version control and source code hosting |

---

## 📁 Project Structure

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

### File and Folder Description

| File or Folder | Description |
|---|---|
| `app.py` | Main Flask application, routes, request handling, and application configuration. |
| `database.py` | Database-related code and database integration. |
| `quiz_data.py` | Quiz questions and related quiz data. |
| `requirements.txt` | Python dependencies required to run the application. |
| `static/css/style.css` | Application styling. |
| `static/js/dashboard.js` | JavaScript functionality associated with the dashboard. |
| `static/js/quiz.js` | JavaScript functionality associated with quizzes. |
| `templates/base.html` | Shared base template for the application's pages. |
| `templates/index.html` | Main landing or dashboard page, depending on the application route. |
| `templates/login.html` | Login page. |
| `templates/register.html` | User registration page. |
| `templates/add_session.html` | Form for adding a practice session. |
| `templates/history.html` | Practice session history page. |
| `templates/quizzes.html` | Quiz browsing page. |
| `templates/take_quiz.html` | Quiz-taking interface. |
| `templates/quiz_result.html` | Quiz results and answer review page. |
| `templates/quiz_history.html` | Previous quiz attempts and results. |
| `.gitignore` | Specifies files and folders that Git should ignore. |

---

## ⚙️ How PrepTrack Works

The application follows a typical Flask web application architecture.

### 1. User Registration and Login

Users can register for an account and log in to access the application's features. Flask handles incoming requests and uses the application's authentication logic to manage user sessions.

### 2. Dashboard Navigation

After accessing the application, users can navigate between the dashboard, practice sessions, study history, and quiz-related pages.

### 3. Practice Session Management

Users can add practice sessions and access their recorded study activities through the history page. The application uses its database layer to manage stored information.

### 4. Quiz Selection and Attempt

Users open the quizzes page, select an available quiz, answer the questions, and submit their responses.

The Flask backend processes the submitted answers and prepares the quiz results.

### 5. Results and Answer Review

After submission, the results page presents the user's score, accuracy, and time taken. It also displays answer-review information, including the user's answers, correct answers, and explanations when available.

Interactive controls make it easier to search, filter, expand, and review quiz questions.

### 6. Reviewing Previous Attempts

Users can visit the quiz history page to access previous quiz attempts and review saved results.

### 7. Database Storage

The application uses SQLite and Flask-SQLAlchemy for data persistence. Application records are stored in database tables so they can be retrieved when users revisit relevant pages.

---

## 🚀 Getting Started

Follow these steps to run PrepTrack on your local machine.

### Prerequisites

Install the following software:

- Python 3.10 or a compatible version.
- pip, the Python package installer.
- Git (optional, for cloning the repository).

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

Navigate into the project directory:

```bash
cd PrepTrack
```

Alternatively, download the repository as a ZIP file and extract it.

### Step 2: Create a Virtual Environment

On Windows:

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### Step 4: Configure the Secret Key

PrepTrack requires a Flask secret key to be provided through an environment variable.

Generate a secure key by running:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the generated value and set it in your current Windows Command Prompt session:

```cmd
set SECRET_KEY=PASTE_YOUR_GENERATED_KEY_HERE
```

Replace the placeholder with the generated key.

**Security note:** Never commit your actual secret key to GitHub. For deployment, configure the secret key through the hosting platform's environment variables.

### Step 5: Run the Application

Start the Flask application:

```bash
python app.py
```

Open the local address displayed in your terminal in your web browser. With Flask's default development settings, this is commonly:

```text
http://127.0.0.1:5000/
```

### Step 6: Start Using PrepTrack

Once the application is running:

1. Register a user account.
2. Log in to the application.
3. Explore the dashboard.
4. Add a practice session.
5. Open the quizzes page and attempt a quiz.
6. Review your score and answers.
7. Visit the history pages to review recorded activities and previous quiz attempts.

---

## 📦 Dependencies

The main dependencies include:

```text
Flask
Flask-SQLAlchemy
```

Install them using:

```bash
pip install -r requirements.txt
```

If the application uses any additional third-party Python packages, add those packages to `requirements.txt` as well.

---

## 🔒 Security and Best Practices

- Keep secret keys and credentials outside the source code.
- Never commit `.env` files containing sensitive information.
- Exclude virtual environments, Python cache files, and local database files from version control when appropriate.
- Use strong passwords when creating accounts.
- Use a production-ready server and disable Flask debug mode when deploying the application.
- Configure environment variables securely in the deployment environment.

---

## 🔮 Future Enhancements

Possible improvements for future versions include:

- Study progress charts and performance analytics.
- Subject-wise and topic-wise performance summaries.
- Study goals and daily progress tracking.
- Quiz difficulty levels and personalized practice.
- Timed quizzes and performance comparisons.
- Improved mobile responsiveness.
- Deployment to a cloud hosting platform.

These are potential future improvements, not necessarily features available in the current version.

---


