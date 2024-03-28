from dataclasses import dataclass


@dataclass
class DBSettings:
    db: str
    user: str
    password: str
    host: str
    port: str
