"""Create pulse_user_owners table. Create keys for other tables.

Revision ID: 4bd0784e2978
Revises: 
Create Date: 2015-05-04 08:44:00.365481

"""

# revision identifiers, used by Alembic.
revision = '4bd0784e2978'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'pulse_user_owners',
        sa.Column('users_id', sa.Integer, sa.ForeignKey('users.id'),
                  nullable=False),
        sa.Column('pulse_users_id', sa.Integer,
                  sa.ForeignKey('pulse_users.id'), nullable=False),
    )

    op.add_column('users',
                  sa.Column('pulse_users', sa.Integer,
                            sa.ForeignKey('pulse_user_owners.users_id')))


def downgrade():
    op.drop_table('pulse_user_owners')
    op.drop_column('users', 'pulse_users')
