import os
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "jee_bot"

_client = None
_db = None


def get_db():
    global _client, _db
    if _db is None:
        _client = AsyncIOMotorClient(MONGO_URI)
        _db = _client[DB_NAME]
    return _db


# ──────────────────────────────────────────────
# User helpers
# ──────────────────────────────────────────────

async def get_user(user_id: int):
    db = get_db()
    user = await db.users.find_one({"user_id": user_id})
    if not user:
        user = {
            "user_id": user_id,
            "study_streak": 0,
            "last_study_date": None,
            "total_study_minutes": 0,
            "joined_at": datetime.utcnow()
        }
        await db.users.insert_one(user)
    return user


async def update_user(user_id: int, update: dict):
    db = get_db()
    await db.users.update_one(
        {"user_id": user_id},
        {"$set": update},
        upsert=True
    )


# ──────────────────────────────────────────────
# Reminder helpers
# ──────────────────────────────────────────────

async def save_reminder(guild_id: int, channel_id: int, user_id: int, exam_name: str, remind_date: datetime):
    db = get_db()
    await db.reminders.insert_one({
        "guild_id": guild_id,
        "channel_id": channel_id,
        "user_id": user_id,
        "exam_name": exam_name,
        "remind_date": remind_date,
        "created_at": datetime.utcnow()
    })


async def get_reminders_for_user(user_id: int):
    db = get_db()
    cursor = db.reminders.find({"user_id": user_id})
    return await cursor.to_list(length=20)


async def delete_reminder(reminder_id):
    db = get_db()
    await db.reminders.delete_one({"_id": reminder_id})
