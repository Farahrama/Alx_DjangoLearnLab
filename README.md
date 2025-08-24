# Social Media API

## Setup
1. Install dependencies:
   pip install django djangorestframework djangorestframework-simplejwt

2. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

3. Create superuser:
   python manage.py createsuperuser

4. Run server:
   python manage.py runserver

## Endpoints
- POST /api/accounts/register/
- POST /api/accounts/login/
- GET/PUT /api/accounts/profile/