from typing import List
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table

# from models.song_model import Song_Model

from models.base_model import Base

class Album_Model(Base):
    __tablename__ = "albums"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String)
    artist: Mapped[str] = Column(String)

    songs: Mapped[List["Songs_to_Albums_Model"]] = relationship(back_populates="playlist")


class Songs_to_Albums_Model(Base):
    __tablename__ = "songs_to_albums"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    song_id: Mapped[int] = mapped_column(ForeignKey("songs.id"))
    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"))

    song: Mapped[List["Song_Model"]] = relationship(back_populates="album")
    playlist: Mapped["Album_Model"] = relationship(back_populates="songs")