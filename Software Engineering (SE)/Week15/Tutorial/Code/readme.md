# Django Blog Project

This project is a simple blog application built with Django. It includes user authentication, groups, and permissions. The application consists of two main apps:

- **authenticate**: Handles user authentication (login, registration) and creates groups via Django signals.
- **blog_app**: Manages blog posts with different permissions for users.

## Prerequisites
Ensure you have the following installed:

- Python (3.x recommended)
- Django (latest stable version)
- SQLite (or another database if preferred)

## Project Setup

### 1. Create a Django Project
#### Windows:
```powershell
mkdir blog_project
cd blog_project
python -m venv venv  # Create a virtual environment
venv\Scripts\activate  # Activate virtual environment
pip install django  # Install Django

# Start a new Django project
django-admin startproject blog_project .
```
#### Linux/Mac:
```bash
mkdir blog_project && cd blog_project
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate virtual environment
pip install django  # Install Django

# Start a new Django project
django-admin startproject blog_project .
```

### 2. Create Django Apps
```bash
python manage.py startapp authenticate
python manage.py startapp blog_app
```

### 3. Add Apps to `settings.py`
Edit `blog_project/settings.py` and add these apps under `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authenticate',
    'blog_app',
]
```

### 4. Configure Authentication Settings
Add these to `settings.py`:
```python
LOGIN_URL = 'login'  # Redirects unauthenticated users to login
LOGIN_REDIRECT_URL = 'index'  # Redirects users after successful login
```

## Migrations and Database Setup
### 1. Run Initial Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Create a Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to enter a username, email, and password.

## Signals for Group and Permission Setup
The `authenticate/signals.py` file creates user groups (`Posters` and `Readers`) and assigns permissions automatically.

### 1. Ensure Signals are Loaded
In `authenticate/apps.py`, update the `ready` method:
```python
from django.apps import AppConfig

class AuthenticateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authenticate'

    def ready(self):
        import authenticate.signals  # Ensures signals are loaded
```

### 2. Run Migrations to Persist Groups & Permissions
```bash
python manage.py makemigrations authenticate
python manage.py migrate
```

## Running the Server
### Windows:
```powershell
python manage.py runserver
```
### Linux/Mac:
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

## Testing Authentication
1. Visit `/admin` and log in with the superuser account.
2. Assign users to groups (`Posters`, `Readers`).
3. Check that `Posters` can add/edit posts, while `Readers` can only view them.

## Conclusion
This project demonstrates Django authentication, permissions, groups, and signals. You can expand it by adding comments, likes, or user profiles!

