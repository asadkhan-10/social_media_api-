# FastAPI Social Media API

A production-structured RESTful API for a social media platform built with FastAPI and PostgreSQL. Covers full CRUD, JWT authentication, a voting system, schema migrations, containerisation, and CI/CD deployment.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI + Uvicorn |
| Database | PostgreSQL |
| ORM | SQLAlchemy 2.0 |
| Migrations | Alembic |
| Validation | Pydantic v2 |
| Auth | JWT (OAuth2 password flow) |
| Containerisation | Docker + Docker Compose |
| CI/CD | GitHub Actions |

---

## Project Structure

```
social_media_api/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── routers/
│   └── ...
├── alembic/
├── tests/
├── .github/
│   └── workflows/
├── Dockerfile
├── docker-compose-dev.yml
├── docker-compose-prod.yml
└── requirements.txt
```

---

## Getting Started

### Option 1 — Docker (Recommended)

```bash
git clone https://github.com/asadkhan-10/social_media_api.git
cd social_media_api
docker-compose -f docker-compose-dev.yml up --build
```

### Option 2 — Manual Setup

```bash
# Clone the repo
git clone https://github.com/asadkhan-10/social_media_api.git
cd social_media_api

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload
```

### Run Migrations

```bash
alembic upgrade head
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_NAME=fastapi
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=yourpassword
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## API Documentation

Once the server is running, visit:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Running Tests

```bash
pytest
```

Tests are also wired into the GitHub Actions CI pipeline and run automatically on every push.

---

## CI/CD

GitHub Actions pipeline runs on every push to `main`:

1. Runs the full `pytest` test suite
2. Builds and validates the Docker image
3. Deploys to production on merge to `main`
