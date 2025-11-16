import os
from dotenv import load_dotenv

load_dotenv()

DB_MAIN_USERNAME = str(os.getenv("DB_MAIN_USERNAME"))
DB_MAIN_PASSWORD = str(os.getenv("DB_MAIN_PASSWORD"))
DB_MAIN_HOST = str(os.getenv("DB_MAIN_HOST"))
DB_MAIN_PORT = str(os.getenv("DB_MAIN_PORT"))
DB_MAIN_DATABASENAME = str(os.getenv("DB_MAIN_DATABASENAME"))
