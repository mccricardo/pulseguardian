"""Create invites table

Revision ID: b27e19d4d63
Revises: 4bd0784e2978
Create Date: 2015-05-07 08:40:08.023642

"""

# revision identifiers, used by Alembic.
revision = 'b27e19d4d63'
down_revision = '4bd0784e2978'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'invites',
        sa.Column('id', sa.Integer, primary_key=True,
                  nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'),
                  nullable=False),
        sa.Column('pulse_user_id', sa.Integer,
                  sa.ForeignKey('pulse_users.id'), nullable=False),
    )


def downgrade():
    op.drop_table('invites')
