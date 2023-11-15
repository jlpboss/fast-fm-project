from typing import List
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table

# from models.song_model import Song_Model

from models.base_model import Base

class Genre_Model(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String)

    songs: Mapped[List["Songs_to_Genres_Model"]] = relationship(back_populates="genre")

class Songs_to_Genres_Model(Base):
    __tablename__ = "songs_to_genres"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    song_id: Mapped[int] = mapped_column(ForeignKey("songs.id"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id"))

    song: Mapped[List["Song_Model"]] = relationship(back_populates="genres")
    genre: Mapped["Genre_Model"] = relationship(back_populates="songs")