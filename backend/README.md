# RetroReel MP Backend

FastAPI backend for RetroReel MP desktop music player.

## Stack

- FastAPI
- SQLAlchemy with SQLite
- Pydantic for schemas

## Changelog

- [Stage 1] Initial setup with SQLAlchemy database configuration and health check endpoint
- [Stage 1] Created SQLAlchemy models: Track, Folder, Playlist, PlaylistTrack, RecentlyPlayed
- [Stage 1] Configured Alembic with sqlite:///./rrmp.db and generated initial migration