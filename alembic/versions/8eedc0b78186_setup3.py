"""setup3

Revision ID: 8eedc0b78186
Revises: b38637048517
Create Date: 2023-11-15 21:59:11.408229

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8eedc0b78186'
down_revision: Union[str, None] = 'b38637048517'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    pass
    # ### end Alembic commands ###
