from typing import Optional
from pydantic import BaseModel
from schemas.song_schema import Song_Schema


class Songs_to_Playlists_Schema(BaseModel):
    id: int
    song_id: int
    playlist_id: int
    order: int


class Playlist_Schema(BaseModel):
    id: int
    name: str
    owner_name: str
    songs: list[Song_Schema]
