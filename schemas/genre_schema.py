from typing import Optional
from pydantic import BaseModel

class Songs_to_Genres_schema(BaseModel):
    id: int
    song_id: int
    genre_id: int

class Genre_Schema(BaseModel):
    id: int
    name: str