# Expense Tracker API

A secure, production-ready RESTful API built with **FastAPI** + **MySQL**, allowing users to track, filter, and manage personal expenses, generate reports, and export data.

---

## Problem Statement

Many people still track their expenses using spreadsheets or manual notes, which are error-prone and offer no insights. This API enables users to record, manage, and analyze their expenses in a clean and efficient way.

---

## Features (MVP)

- User registration and JWT-based login
- Add, update, delete, and view expenses
- Categorize expenses
- Filter expenses by date and category
- Monthly expense summary reports
- Export data to CSV
- Secure, token-protected endpoints

---

## 👤 User Stories

- As a user, I want to register and log in to track my expenses securely.
- As a user, I want to view all my expenses by date and category.
- As a user, I want to add, update, and delete my own expenses.
- As a user, I want to download my expenses as a CSV file.
- As a user, I want to see monthly summaries to understand my spending.

---

## API Endpoints (Planned)

```
POST    /auth/register          # User registration
POST    /auth/login             # JWT token login
GET     /me                     # Get current user info

POST    /expenses               # Add a new expense
GET     /expenses               # Get all expenses (with filters)
GET     /expenses/{id}          # Get a single expense
PUT     /expenses/{id}          # Update expense
DELETE  /expenses/{id}          # Delete expense

GET     /reports/summary        # Get monthly summary
GET     /reports/export         # Export expenses to CSV
```

---

## Data Model

```
User
- id
- email
- hashed_password

Expense
- id
- user_id (FK)
- amount
- category
- date
- note

Category
- id
- name
```

---

## Tech Stack

- **FastAPI** – Web framework
- **MySQL** – Database
- **SQLAlchemy + Alembic** – ORM + Migrations
- **JWT (python-jose)** – Auth tokens
- **Pydantic** – Data validation
- **Pytest** – Testing
- **Docker** – Containerization
- **Fly.io / Railway** – Deployment

---

## Environment Variables

Create a `.env` file in the project root (do NOT commit it).  
Use `.env.example` as a reference.

```
DATABASE_URL=
SECRET_KEY=
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Run the Project (Dev)

```bash
# Activate virtual environment
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
```

---

## Security & Auth

- Passwords are hashed (bcrypt)
- JWT tokens used for secure access
- All user-specific data is isolated

---

## Deployment Plan (Coming Soon)

- Dockerize the app
- Add production environment configs
- Deploy to Fly.io or Railway with CI/CD

---

## License

MIT License – free to use, modify, and share with attribution.

---

## Showcase (Planned)

- Loom or video demo of API in action
- Swagger screenshots of endpoints
- GitHub + Live API link
