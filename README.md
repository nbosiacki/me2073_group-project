# Campus Marketplace

A community marketplace web app for student dorm residents. Connect with your campus neighbors to buy, sell, trade goods and offer services — with sustainability and waste reduction in mind.

**Stack:** Python (FastAPI) · React (Vite) · MongoDB

---

## Prerequisites

- Python 3.12+
- Node.js 20+
- Docker (for MongoDB)

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/nbosiacki/me2073_group-project.git
cd me2073_group-project
```

### 2. Environment variables

```bash
cp .env.example .env
```

Edit `.env` and set your values (defaults work for local development):

| Variable | Default | Description |
|----------|---------|-------------|
| `MONGODB_URL` | `mongodb://localhost:27017` | MongoDB connection string |
| `DB_NAME` | `campus_marketplace` | Database name |
| `JWT_SECRET` | `dev-secret-change-in-prod` | Secret for signing JWT tokens |
| `JWT_EXPIRY_HOURS` | `24` | Token expiry time in hours |

### 3. Backend setup

```bash
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

pip install -r backend/requirements-dev.txt
```

### 4. Frontend setup

```bash
cd frontend
npm install
cd ..
```

## Startup

### Start MongoDB

```bash
docker run -d --name campus-mongo -p 27017:27017 -v campus-mongo-data:/data/db mongo:7
```

This starts MongoDB in the background with a named volume for persistent data. The default `MONGODB_URL` in `.env.example` already points to `localhost:27017`.

### Start the backend

```bash
source venv/bin/activate
cd backend
uvicorn app.main:app --reload --port 8000
```

The API will be available at http://localhost:8000. Interactive docs at http://localhost:8000/docs.

### Start the frontend

In a separate terminal:

```bash
cd frontend
npm run dev
```

The app will be available at http://localhost:5173. API requests to `/api/*` are proxied to the backend automatically.

## Shutdown

1. **Frontend:** `Ctrl+C` in the frontend terminal
2. **Backend:** `Ctrl+C` in the backend terminal
3. **MongoDB:** `docker stop campus-mongo`

To restart MongoDB later: `docker start campus-mongo`

To remove the container (data is preserved in the volume): `docker rm campus-mongo`

To remove the data volume entirely: `docker volume rm campus-mongo-data`

## Running Tests

### Backend

```bash
source venv/bin/activate
cd backend
pytest -v
```

### Frontend

```bash
cd frontend
npm test
```

## Project Structure

```
me2073_group-project/
  backend/
    app/
      main.py          # FastAPI application
      config.py         # Environment variable loading
      models/           # Pydantic models
      routers/          # API route handlers
      services/         # Business logic
      middleware/        # Auth and other middleware
      schemas/          # DB indexes and schemas
    tests/              # pytest test suite
  frontend/
    src/                # React application source
    tests/              # Vitest test suite
  scripts/              # Dev tools and seed data scripts
```
