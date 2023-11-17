from sqlalchemy.orm import Session, aliased, joinedload
from models.import_modles import User_Model, Playlist_Model ,Songs_to_Playlists_Model, Song_Model
from schemas.import_schemas import User_Schema, Playlist_Schema, Song_Schema
from sqlalchemy import and_, or_

def create_user(db: Session, user_schema: User_Schema):
    user = User_Model(
        username = user_schema.username, 
        fullname = user_schema.fullname, 
        email = user_schema.email,
        hashed_password = user_schema.hashed_password
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db: Session):
    query = (
        db.query(User_Model)
        .options(
            joinedload(User_Model.playlists).joinedload(Playlist_Model.songs).joinedload(Songs_to_Playlists_Model.song).joinedload(Song_Model.playlist)
        )
        .all()
    )
    items = {}

    for item in query:
        user_id = item.id
        user_item_schema = User_Schema(
            id = item.id,
            username = item.username,
            fullname = item.fullname,
            email = item.email,
            hashed_password = item.hashed_password,
            playlist = [
                Playlist_Schema(
                    id = playlist.id,
                    name = playlist.name,
                    # songs = [
                    #         Song_Schema(
                    #             id = song.id,
                    #             title = song.title,
                    #             artist = song.artist,
                    #             duration = song.duration,
                    #             release = sond.release
                    #         )
                    #     ] 
                    #     for song in playlist.songs.song
                )
                for playlist in item.playlists
            ]
        )
        items[user_id] = user_item_schema

    out = list(items.values())
    return out

def remove_user(db: Session, id: int):
    user = (
        db.query(User_Model)
        .options(
            joinedload(User_Model.playlists).joinedload(Playlist_Model.songs).joinedload(Songs_to_Playlists_Model.song).joinedload(Song_Model.playlist)
        )
        .filter(User_Model.id == id)
        .first()
    )
    user_copy = user
    db.delete(user)
    db.commit()
    return user_copy