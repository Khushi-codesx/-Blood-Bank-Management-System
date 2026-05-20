# Blood Bank Management System - Complete Django Project

## Features
- Admin registration and login
- Donor form with automatic blood stock update
- Patient blood request form
- Admin dashboard with total donors, patients, requests and stock units
- Approve/reject blood requests
- Blood stock list
- Donation/approved records
- Contact and feedback forms
- Django admin panel

## Setup
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open: http://127.0.0.1:8000/

Django admin URL: http://127.0.0.1:8000/django-admin/
Create superuser:
```bash
python manage.py createsuperuser
```

## Main URLs
- `/` Home
- `/register/` Admin registration
- `/admin-login/` Admin login
- `/admindashboard/` Dashboard
- `/donarform/` Donor form
- `/patient/` Patient blood request
- `/bloodstock/` Blood stock
- `/bloodrequest/` Manage requests
