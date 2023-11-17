from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from schemas.genre_schema import Genre_Schema

class Song_Schema(BaseModel):
    id: int
    title: str
    artist: str
    duration: float
    release: datetime | None = None
    genres: list[Genre_Schema] | None = []
