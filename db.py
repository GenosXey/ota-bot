# app/db.py

from pymongo import MongoClient
from app.config import MONGO_URI, DB_NAME

mongo = MongoClient(MONGO_URI)
db = mongo[DB_NAME]
users_col = db["users"]

def get_user(user_id: int):
    return users_col.find_one({"_id": user_id})

def create_user(user_id: int, username: str, referred_by: int = None):
    if not get_user(user_id):
        user_data = {
            "_id": user_id,
            "username": username,
            "points": 0,
            "referrals": 0,
            "referred_by": referred_by
        }
        users_col.insert_one(user_data)
        if referred_by and get_user(referred_by):
            users_col.update_one({"_id": referred_by}, {
                "$inc": {"points": 5, "referrals": 1}
            })

def increment_points(user_id: int, points: int = 3):
    users_col.update_one({"_id": user_id}, {"$inc": {"points": points}})

def get_points(user_id: int):
    user = get_user(user_id)
    return user["points"] if user else 0

def get_referral_count(user_id: int):
    user = get_user(user_id)
    return user["referrals"] if user else 0
