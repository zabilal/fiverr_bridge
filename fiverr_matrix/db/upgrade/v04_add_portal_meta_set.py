from mautrix.util.async_db import Connection

from . import upgrade_table


@upgrade_table.register(description="Add name_set, avatar_set, and topic_set to portals")
async def upgrade_v4(conn: Connection):
    await conn.execute("ALTER TABLE portal ADD COLUMN name_set BOOLEAN NOT NULL DEFAULT false")
    await conn.execute("ALTER TABLE portal ADD COLUMN avatar_set BOOLEAN NOT NULL DEFAULT false")
    await conn.execute("ALTER TABLE portal ADD COLUMN topic_set BOOLEAN NOT NULL DEFAULT false")
    await conn.execute("UPDATE portal SET name_set=true WHERE name<>''")
    # We don't set avatar_set to true because there was a bug that caused avatars to
    # be set incorrectly, so we want everything to be reset.
    # We also don't set topic_set to true because none of the topics have been
    # stored in the database due to a bug.
