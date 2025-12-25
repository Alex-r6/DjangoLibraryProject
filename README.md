DjangoLibraryProject is a simple Django project that implements a basic library system for managing books and users. It demonstrates working with models, forms, templates, authentication, and basic CRUD operations.

Features

Add, edit, and delete books

View a list of books

User registration and login

Simple library management via web interface and Django admin

Technologies

Python 3.x

Django 4.x

SQLite (default, can be replaced with PostgreSQL)

HTML, CSS (Django templates)

Installation (Development)
git clone https://github.com/Alex-r6/DjangoLibraryProject.git
cd DjangoLibraryProject
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Open http://127.0.0.1:8000/ in your browser.

Production Setup

Install a production-ready database (PostgreSQL recommended)

Configure ALLOWED_HOSTS and DATABASES in settings.py

Use gunicorn or uwsgi with Nginx for deployment

Collect static files:

python manage.py collectstatic


Apply migrations and start the production server

Project Structure
DjangoLibraryProject/
├── project2/           # Main Django app
│   ├── migrations/     
│   ├── templates/      
│   ├── static/         
│   ├── models.py       
│   ├── views.py        
│   └── urls.py         
├── manage.py           
└── requirements.txt    

Usage

Register or login, add books via the interface, and manage the library using the web interface or Django admin.

License

Open-source, free for learning and personal use.
