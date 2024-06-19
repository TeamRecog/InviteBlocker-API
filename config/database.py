import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_APPNAME = os.getenv("DB_APPNAME")

client = MongoClient(
    f"mongodb+srv://{DB_USER}:{DB_PASS}@{DB_HOSTNAME}/?retryWrites=true&w=majority&appName={DB_APPNAME}")

db = client.smc_db

collection_name = db["sites_collection"]
