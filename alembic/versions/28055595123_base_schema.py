"""Base schema.

Revision ID: 28055595123
Revises: b27e19d4d63
Create Date: 2015-07-27 08:52:27.417078

"""

# revision identifiers, used by Alembic.
revision = '28055595123'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'pulse_users',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('owner_id', sa.Integer),
        sa.Column('username', sa.String(255))
    )

    op.create_table(
        'queues',
        sa.Column('name', sa.String(255)),
        sa.Column('owner_id', sa.Integer),
        sa.Column('size', sa.Integer),
        sa.Column('warned', sa.Integer)
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('email', sa.String(255)),
        sa.Column('admin', sa.Integer)
    )


def downgrade():
    op.drop_table('pulse_users')
    op.drop_table('queues')
    op.drop_table('users')
