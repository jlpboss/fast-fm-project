from typing import List
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table

# from models.playlist_model import Playlist_Model

from models.base_model import Base

class User_Model(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = Column(String, unique=True)
    fullname: Mapped[str] = Column(String)
    email: Mapped[str] = Column(String, unique=True)
    hashed_password: Mapped[str] = Column(String)

    playlists:Mapped[List["Playlist_Model"]] = relationship(
        back_populates="owner", cascade="all, delete-orphan")

# Fix to use id not email