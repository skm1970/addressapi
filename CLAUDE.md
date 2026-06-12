# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the dev server (auto-reload on file changes)
.venv\Scripts\activate
uvicorn main:app --reload

# API docs (Swagger UI) once server is running
# http://localhost:8000/docs
```

## Architecture

Four-file FastAPI app with in-memory storage:

- **`models.py`** — Pydantic models: `AddressBase`, `AddressCreate` (includes `name`), `AddressUpdate` (all fields optional), `Address` (response shape).
- **`storage.py`** — Module-level `db: dict[str, Address]` dict. All persistence logic lives here (`add`, `get`, `get_all`, `update`, `delete`).
- **`routes.py`** — `APIRouter` with all five `/addresses` endpoints. Imports `storage` directly (not injected).
- **`main.py`** — Creates the `FastAPI` app and mounts the router.

## Endpoints

| Method | Path | Notes |
|--------|------|-------|
| POST | `/addresses/` | 409 if `name` already exists |
| GET | `/addresses/` | Returns all addresses |
| GET | `/addresses/{name}` | 404 if not found |
| PUT | `/addresses/{name}` | Partial update; 404 if not found |
| DELETE | `/addresses/{name}` | 204 on success; 404 if not found |

- Azure deployment URL - https://addressapps-cbf5ebhbg4dpe0cn.eastus-01.azurewebsites.net/
`name` is the unique key — it is part of the request body on create and the URL path on all other operations.

## Key Constraints

- Storage is in-memory only; all data is lost on server restart.
- `name` is immutable after creation — updating a record does not change its key in `db`.
