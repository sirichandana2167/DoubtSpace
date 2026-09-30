
# DoubtSpace - Anonymous Student Doubt Forum

## About the Project
DoubtSpace is a web-based platform where students can ask academic questions and help one another by sharing answers anonymously. It provides a simple and user-friendly environment for collaborative learning.

## Problem Statement
Students often hesitate to ask questions in classrooms because of fear, lack of confidence, or concern about being judged. DoubtSpace provides a platform where students can ask doubts anonymously and receive help from their peers.

## Objectives
- Encourage students to ask academic questions.
- Enable students to share knowledge through answers.
- Organize doubts by subject category.
- Help students find questions using search and filters.
- Support community participation through upvotes.

## Features
- Student registration and login
- Anonymous question posting
- Academic categories
- Search and category filtering
- Answer submission
- One upvote per account per question
- Responsive user interface
- Django admin interface for management

## Technology Stack

**Frontend**
- HTML
- CSS
- Bootstrap

**Backend**
- Python
- Django

**Database**
- SQLite

**Tools**
- Visual Studio Code
- Git
- GitHub

## Project Structure

```text
doubtforum/
├── doubtforum/
├── forum/
├── static/
├── templates/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd doubtforum
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

### 7. Open the application

Visit:

http://127.0.0.1:8000/

Register an account to explore the platform.

## Future Enhancements
- Improved moderation tools
- Notifications for new answers
- User profiles and reputation
- Additional search and filtering options

## Conclusion
DoubtSpace aims to make academic collaboration easier by giving students a platform to ask questions, share knowledge, and learn together in an anonymous environment.

## Developed As
Full Stack Development (FSD) Academic Project