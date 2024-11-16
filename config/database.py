from pymongo.mongo_client import MongoClient
from utils import env

client = MongoClient(
    f"mongodb+srv://{env.DB_USER}:{env.DB_PASS}@{env.DB_HOSTNAME}/?retryWrites=true&w=majority&appName={env.DB_APPNAME}")

db = client.invblock_db

invites_collection = db["invites_collection"]
