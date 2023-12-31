"""setup4

Revision ID: aea3e8a66d5b
Revises: 8eedc0b78186
Create Date: 2023-11-16 15:34:53.663396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aea3e8a66d5b'
down_revision: Union[str, None] = '8eedc0b78186'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('artist', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_albums_id'), 'albums', ['id'], unique=False)
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_genres_id'), 'genres', ['id'], unique=False)
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('artist', sa.String(), nullable=True),
    sa.Column('duration', sa.Float(), nullable=True),
    sa.Column('release', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_songs_id'), 'songs', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('playlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('owner_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['owner_name'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_playlists_id'), 'playlists', ['id'], unique=False)
    op.create_table('songs_to_albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_songs_to_albums_id'), 'songs_to_albums', ['id'], unique=False)
    op.create_table('songs_to_genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_songs_to_genres_id'), 'songs_to_genres', ['id'], unique=False)
    op.create_table('songs_to_playlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('playlist_id', sa.Integer(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlists.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_songs_to_playlists_id'), 'songs_to_playlists', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_songs_to_playlists_id'), table_name='songs_to_playlists')
    op.drop_table('songs_to_playlists')
    op.drop_index(op.f('ix_songs_to_genres_id'), table_name='songs_to_genres')
    op.drop_table('songs_to_genres')
    op.drop_index(op.f('ix_songs_to_albums_id'), table_name='songs_to_albums')
    op.drop_table('songs_to_albums')
    op.drop_index(op.f('ix_playlists_id'), table_name='playlists')
    op.drop_table('playlists')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_songs_id'), table_name='songs')
    op.drop_table('songs')
    op.drop_index(op.f('ix_genres_id'), table_name='genres')
    op.drop_table('genres')
    op.drop_index(op.f('ix_albums_id'), table_name='albums')
    op.drop_table('albums')
    # ### end Alembic commands ###
