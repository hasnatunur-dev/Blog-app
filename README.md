Blog App
A Django-based blogging platform built to practice backend web development, database integration, and user-facing web application features.

Overview
Blog App is a web application for publishing and managing blog content. It is designed with Python and Django


Features
•	Blog Post Management — Create, view, edit, and delete blog posts.
•	User Registration & Login — Allow users to create accounts and log in.
•	Post Likes — Allow users to like blog posts.
•	Post Views — Display the number of views for each blog post.
•	Comments — Allow users to comment on blog posts.
•	Comment Replies — Allow users to reply to comments and interact with other users.
•	Database Integration — Store blog posts, users, likes, comments, replies, and view counts.
•	Django Templates — Render dynamic blog content using Django templates.


Tech Stack
•	Backend: Python, Django
•	Database: Specify your actual database
•	Frontend: Specify your actual frontend technologies
•	Version Control: Git and GitHub

Getting Started
Prerequisites
•	Python 3.12 or a compatible version
•	Git
•	pip

Installation
1.	Clone the repository:
2.	git clone https://github.com/hasnatunur-dev/Blog-app.git
cd Blog-app
3.	Create a virtual environment:
python -m venv venv
4.	Activate it on Windows:
venv\Scripts\activate
5.	Install dependencies:
pip install -r requirements.txt
6.	Navigate to the directory containing manage.py, if necessary, and run:
7.	python manage.py migrate
python manage.py runserver
8.	Open http://127.0.0.1:8000/ in your browser.



## Project Structure
```text
Blog-app/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── blog/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── blogapp/
    ├── migrations/
    ├── templates/
    ├── static/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── tests.py
```
# File and Folder Descriptions

- `manage.py` — Runs Django management commands and starts the development server.
- `requirements.txt` — Lists the Python packages required to run the project.
- `README.md` — Documents the project, features, and installation instructions.
- `.gitignore` — Specifies files Git should ignore, such as virtual environments and Python cache files.
- `blog/` — Contains the Django project configuration, settings, and main URL routing.
- `blogapp/` — Contains the blog application's models, views, URLs, templates, and tests.
- `migrations/` — Stores database schema migration files.
- `templates/` — Contains HTML templates used to render web pages.
- `static/` — Contains CSS, JavaScript, and image files.





What I Learned
•	Building web applications with Django
•	Working with databases and models
•	Managing project dependencies
•	Using Git and GitHub for version control


Author
Hasnatun Nur
•	GitHub: @hasnatunur-dev


