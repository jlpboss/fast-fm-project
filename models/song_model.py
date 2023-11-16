from typing import List
from typing import Optional
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Float, DateTime

# from models.playlist_model import Songs_to_Playlists_Model
# from models.album_model import Songs_to_Albums_Model
# from models.genre_model import Songs_to_Genres_Model

from models.base_model import Base

class Song_Model(Base):
    __tablename__ = "songs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = Column(String)
    artist: Mapped[str] = Column(String)
    duration: Mapped[float] = Column(Float)
    release: datetime = Column(DateTime)

    playlist: Mapped[List["Songs_to_Playlists_Model"]] = relationship(back_populates="song")
    album: Mapped[List["Songs_to_Albums_Model"]] = relationship(back_populates="song")
    genre: Mapped[List["Songs_to_Genres_Model"]] = relationship(back_populates="song")
