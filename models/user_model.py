from typing import List
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table

from playlist_model import Playlist_Model

from base_model import Base

class User_Model(Base):
    __tablename__ = "users"

    username: Mapped[str] = Column(String)
    fullname: Mapped[str] = Column(String)
    email: Mapped[str] = mapped_column(primary_key=True)
    hashed_password: Mapped[str] = Column(String)

    playlists:Mapped[List["Playlist_Model"]] = relationship(
        back_populates="owner", cascade="all, delete-orphan")