from dotenv import load_dotenv

from .db_settings import load_db_settings


load_dotenv()

db_settings = load_db_settings()
