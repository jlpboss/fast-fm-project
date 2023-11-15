from typing import List
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table

from user_model import User_Model
from song_model import Song_Model

from base_model import Base

class Playlist_Model(Base):
    __tablename__: "playlists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String)
    owner_name: Mapped[str] = mapped_column(ForeignKey("users.username"))

    owner:Mapped["User_Model"] = relationship(back_populates="playlists")
    songs: Mapped[List["Songs_to_Playlists_Model"]] = relationship(back_populates="song")
    
class Songs_to_Playlists_Model(Base):
    __tablename__: "songs_to_playlists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    song_id: Mapped[int] = mapped_column(ForeignKey("songs.id"))
    playlist_id: Mapped[int] = mapped_column(ForeignKey("playlists.id"))
    order: Mapped[int] = Column(Integer)

    song: Mapped[List["Song_Model"]] = relationship(back_populates="playlist")
    playlist: Mapped["Playlist_Model"] = relationship(back_populates="owner")
