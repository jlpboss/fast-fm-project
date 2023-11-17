from typing import Optional
from pydantic import BaseModel
from schemas.song_schema import Song_Schema

class Songs_to_Albums_schema(BaseModel):
    id: int
    song_id: int
    album_id: int

class Album_Schema(BaseModel):
    id: int
    name: str
    artist: str
    songs: list[Song_Schema]