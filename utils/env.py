import os
from dotenv import load_dotenv

load_dotenv()

ANALYTICS_API_KEY = os.getenv("ANALYTICS_API_KEY")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_APPNAME = os.getenv("DB_APPNAME")
