#  Django JWT Authentication API

A secure backend REST API built with Django REST Framework and JWT (JSON Web Token) authentication using `djangorestframework-simplejwt`. It includes user registration, login, access-protected routes, and token refreshing.

---

## Features

- User Registration (with email & password validation)
- JWT-based Login (`access` & `refresh` tokens)
- Token Refresh Endpoint
- Protected Dashboard Route (requires valid access token)
- Input validation & error handling

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/jwt_auth_project.git
cd jwt_auth_project
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not present, run:
```bash
pip install django djangorestframework djangorestframework-simplejwt
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the server

```bash
python manage.py runserver
```

### 6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

---

## 🔗 API Endpoints

| Method | Endpoint                 | Description                |
|--------|--------------------------|----------------------------|
| POST   | `/api/register/`         | Register new user          |
| POST   | `/api/login/`            | Obtain JWT access/refresh  |
| POST   | `/api/token/refresh/`    | Refresh access token       |
| GET    | `/api/dashboard/`        | Protected route (JWT only) |

---

##  Sample Login Payload

```json
{
  "username": "username",
  "password": "TestPass123"
}
```

---

##  Authorization Header Format

To access protected routes (e.g., `/api/dashboard/`), include:

```http
Authorization: Bearer <access_token>
```

---

##  Folder Structure

```
jwt_auth_project/
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── jwt_auth_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

