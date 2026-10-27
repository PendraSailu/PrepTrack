# PrepTrack – Learning and Preparation Tracker

PrepTrack is a web application designed to help users organize their learning and monitor their preparation progress.

## Features

- User registration and login
- Password hashing and validation
- Personalized learning dashboard
- Manual practice session tracking
- Subject-wise performance analysis
- Interactive quizzes with a timer
- Quiz results and answer explanations
- Practice history and quiz history
- Topic-wise performance recommendations

## Technologies Used

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML
- CSS
- JavaScript

## Getting Started

### 1. Clone the repository

Clone this repository to your local machine.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows Command Prompt:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the secret key

Set a secure `SECRET_KEY` environment variable before running the application.

Windows Command Prompt:

```bash
set SECRET_KEY=your-generated-secret-key
```

Replace the example value with a securely generated secret. Never commit it to GitHub.

### 6. Run the application

```bash
python app.py
```

Open the local address displayed in your terminal in your web browser.

## Database

PrepTrack uses SQLite for data storage. The application initializes its database when it starts. Existing database files and private user data should not be committed to a public repository.