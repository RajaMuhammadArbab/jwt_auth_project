#  Sample Postman API Requests

##  1. Register a New User
**Method:** `POST`  
**URL:** `http://localhost:8000/api/register/`  
**Body (raw JSON):**
```json
{
  "username": "xyz",
  "email": "xyz@example.com",
  "password": "TestPass123"
}
```

---

##  2. Login to Get JWT Token
**Method:** `POST`  
**URL:** `http://localhost:8000/api/login/`  
**Body (raw JSON):**
```json
{
  "username": "xyz",
  "password": "TestPass123"
}
```

**Response Example:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1..."
}
```

---

##  3. Refresh JWT Token
**Method:** `POST`  
**URL:** `http://localhost:8000/api/token/refresh/`  
**Body (raw JSON):**
```json
{
  "refresh": "paste_your_refresh_token_here"
}
```

---

## 4. Access Protected Dashboard
**Method:** `GET`  
**URL:** `http://localhost:8000/api/dashboard/`  
**Headers:**
```
Key: Authorization
Value: Bearer paste_your_access_token_here
```

**Response (if valid):**
```json
{
  "message": "Welcome to your dashboard xyz"
}
```

**Response (if token is missing or invalid):**
```json
{
  "detail": "Authentication credentials were not provided."
}
```
