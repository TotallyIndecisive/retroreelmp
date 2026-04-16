# RetroReel MP

A Linux desktop music player built with Python FastAPI, Vue 3, and pywebview.

## Tech Stack

- **Backend:** Python, FastAPI, SQLAlchemy, SQLite
- **Frontend:** Vue 3, Vite, Tailwind CSS
- **Desktop:** pywebview (wraps web UI in native window)

## Prerequisites

- Python 3.10+
- Node.js 20+
- uv (Python package manager)
- GTK/webkit system libraries (for pywebview on Linux)

## Setup

```bash
# Clone and enter project
cd rrmp

# Install Python dependencies
uv sync

# Build frontend
cd frontend && npm install && npm run build && cd ..

# Run the app
.venv/bin/python main.py
```

## Project Structure

```
rrmp/
├── main.py           # App entry point (FastAPI + pywebview)
├── backend/          # FastAPI backend
│   ├── db.py        # SQLAlchemy setup
│   ├── models/      # Database models
│   ├── routers/    # API endpoints
│   └── schemas/     # Pydantic schemas
└── frontend/         # Vue 3 frontend
    ├── src/         # Vue components
    └── dist/        # Built assets
```

## Changelog

- [Stage 1] Initial project setup with FastAPI, Vue 3, pywebview, and Tailwind CSS
- [Stage 1] Database models: Track, Folder, Playlist, PlaylistTrack, RecentlyPlayed with Alembic migrations