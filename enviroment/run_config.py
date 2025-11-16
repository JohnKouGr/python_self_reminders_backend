import os
from dotenv import load_dotenv

load_dotenv()

FLASK_APP = "python self reminders back end"
FLASK_DEBUG = bool(os.getenv("FLASK_DEBUG"))
FLASK_PORT = str(os.getenv("FLASK_PORT")) 
FLASK_HOST = str(os.getenv("FLASK_HOST"))

