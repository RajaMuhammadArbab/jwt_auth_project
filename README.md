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

## Project Demo

<img width="1403" height="841" alt="1" src="https://github.com/user-attachments/assets/fdabade8-dcc6-4f33-a1a3-fc4a6a3af5b5" />
<img width="1392" height="837" alt="2" src="https://github.com/user-attachments/assets/cc32587c-2fd8-4dc5-a0be-861f23346e71" />
<img width="1385" height="785" alt="3" src="https://github.com/user-attachments/assets/56f8771c-66e3-4a1f-85c5-416dd6d9ada8" />
<img width="1392" height="840" alt="4" src="https://github.com/user-attachments/assets/4c7a8aae-f779-4e98-8253-e67e21f34b20" />
<img width="773" height="321" alt="5" src="https://github.com/user-attachments/assets/b984dfeb-4fd1-452b-91aa-245e59ea4157" />
<img width="1382" height="765" alt="6" src="https://github.com/user-attachments/assets/3af7cab4-5aac-4445-8be2-535ce1b6b491" />

<img width="773" height="321" alt="5" src="https://github.com/user-attachments/assets/c6271e76-218f-462a-8400-0b110ab6141b" />
<img width="1382" height="765" alt="6" src="https://github.com/user-attachments/assets/cf5df0c4-9ee7-4cf5-9eea-50a0ab6459b0" />
