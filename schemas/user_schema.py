from typing import Optional
from pydantic import BaseModel
from schemas.playlist_schema import Playlist_Schema

class User_Schema(BaseModel):
    id: int
    username: str
    fullname: str
    email: str
    hashed_password: str
    playlist: list[Playlist_Schema] | None = []