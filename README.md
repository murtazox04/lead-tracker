# 📋 Lead Tracker API

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/downloads/release/python-3110/)
[![Django](https://img.shields.io/badge/Django-5.2-success)](https://docs.djangoproject.com/en/5.2/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#tests)
[![Dockerized](https://img.shields.io/badge/docker-ready-blue)](https://www.docker.com/)
[![Swagger](https://img.shields.io/badge/docs-swagger-blue)](#swagger)

---

## 🧠 Project Description

**Lead Tracker API** is a backend system to:

- Receive **lead submissions** via a public API (with first name, last name, email, and resume).
- Send **email notifications** to both the prospect and an internal attorney.
- Allow **authenticated internal users** to:
  - View the list of leads.
  - Mark leads as _REACHED_OUT_.

> The API is built using Django 5.2, Django REST Framework (DRF), PostgreSQL, and DRF-YASG for Swagger support.

---

## 🚀 Tech Stack

- **Python** 3.11
- **Django** 5.2
- **DRF** (Django REST Framework)
- **PostgreSQL**
- **Docker & docker-compose**
- **DRF-YASG** for Swagger UI

---

## 🧪 Running Tests

You can run all tests inside Docker using:

```bash
docker compose run test
```

✅ The following things are tested:

- Model creation
- Public API lead submission
- Email sending
- Authenticated API list + patch
- File upload logic

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/murtazox04/lead-tracker.git
cd lead-tracker
```

### 2. Create `.env` file

```bash
cp .env.example .env
```

Fill in your environment values (especially DB and email settings).

---

### 3. Run with Docker

```bash
docker compose up --build
```

The app will be available at:  
📍 `http://localhost:8000`

---

## 🔐 Authentication

Internal endpoints require Django session or basic auth.  
For testing, you can create a superuser:

```bash
docker compose exec web python manage.py createsuperuser
```

---

## 📂 API Endpoints

| Method | URL                                  | Auth Required | Description                |
| ------ | ------------------------------------ | ------------- | -------------------------- |
| POST   | `/api/leads/create/`                 | ❌ No         | Public lead form           |
| GET    | `/api/leads/`                        | ✅ Yes        | List all submitted leads   |
| PATCH  | `/api/leads/<uuid:pk>/mark-reached/` | ✅ Yes        | Mark lead as `REACHED_OUT` |

---

## 🧾 Email Notifications

When a new lead is submitted:

- ✅ Prospect receives a confirmation email.
- ✅ Internal attorney receives a new lead alert.

Email backend is configured via `.env`.

---

## 📑 Swagger

📍 Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)  
📍 ReDoc UI: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

## 📁 Project Structure

```
lead-tracker/
├── config/                # Django project config
├── leads/                 # Main app: views, models, serializers, tests, email templates
├── media/                 # Uploaded resumes
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🛠 Useful Commands

### Create DB migrations

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

### Collect static files

```bash
docker compose exec web python manage.py collectstatic --noinput
```

---

## 📬 Contact

Developed by **Murtazo Xurramov** — [LinkedIn](https://linkedin.com/in/murtazo-xurramov) | [GitHub](https://github.com/murtazox04)

> Made with ❤️ for a technical assignment.
