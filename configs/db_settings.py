import os
from .schemas import DBSettings


def load_db_settings() -> DBSettings:
    """Function for loading db settings"""
    db = os.getenv("POSTGRES_DB")
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")

    if (
            (db is None) or (user is None) or (password is None)
            or (host is None) or (port is None)
    ):
        raise TypeError("Database configs are not filled in.")

    return DBSettings(
        db=db,
        user=user,
        password=password,
        host=host,
        port=port,
    )
