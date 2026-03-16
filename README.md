# 📚 JEE Discord Bot

A lightweight, focused Discord bot for **JEE Main & Advanced** aspirants. Built with `discord.py` + MongoDB.

---

## ✨ Features

| Feature | Commands |
|--------|----------|
| 📖 Study Resources | `!notes`, `!notes <subject>`, `!notes <subject> <topic>` |
| 📋 Syllabus | `!syllabus`, `!syllabus <subject>` |
| 📅 Exam Dates | `!schedule`, `!schedule main`, `!schedule advanced` |
| ⏳ Countdown | `!countdown` |
| 🔔 Reminders | `!remind <exam>`, `!myreminders` |
| ❓ Help | `!help`, `!ping` |

---

## 🗂️ Project Structure

```
jee_bot/
├── bot.py                 # Entry point, task loops
├── requirements.txt
├── .env.example           # Copy to .env and fill in
├── cogs/
│   ├── notes.py           # !notes, !syllabus
│   ├── schedule.py        # !schedule, !countdown, !remind
│   └── help.py            # !help, !ping
└── utils/
    ├── db.py              # MongoDB (motor async)
    └── exam_data.py       # Exam dates + resource links
```

---

## 🚀 Setup (Local)

### 1. Clone & install dependencies
```bash
git clone <your-repo>
cd jee_bot
pip install -r requirements.txt
```

### 2. Configure environment
```bash
cp .env.example .env
# Open .env and fill in DISCORD_TOKEN and MONGO_URI
```

### 3. Get your Discord Bot Token
1. Go to https://discord.com/developers/applications
2. Click **New Application** → name it (e.g. "JEE Bot")
3. Go to **Bot** tab → **Reset Token** → copy it
4. Under **Privileged Gateway Intents**, enable:
   - ✅ Server Members Intent
   - ✅ Message Content Intent
5. Go to **OAuth2 → URL Generator** → check `bot` → check permissions:
   - Send Messages, Embed Links, Read Message History, Add Reactions
6. Copy the generated URL and invite the bot to your server

### 4. Get your MongoDB URI
1. Go to https://www.mongodb.com/atlas → create a free cluster
2. Click **Connect** → **Drivers** → copy the connection string
3. Replace `<password>` with your DB user's password
4. Paste it as `MONGO_URI` in your `.env`

### 5. Run the bot
```bash
python bot.py
```

---

## ☁️ Hosting on Railway (Free)

1. Push your code to GitHub (don't commit `.env`)
2. Go to https://railway.app → New Project → Deploy from GitHub
3. Add environment variables in Railway's dashboard:
   - `DISCORD_TOKEN`
   - `MONGO_URI`
4. Railway auto-detects Python and runs `bot.py`

---

## ☁️ Hosting on Replit

1. Create a new Replit Python project
2. Upload all files
3. In **Secrets** (🔒 tab), add `DISCORD_TOKEN` and `MONGO_URI`
4. Click Run — use [UptimeRobot](https://uptimerobot.com) to keep it alive 24/7

---

## 🔔 How Reminders Work

The bot runs a **daily background task** (`check_reminders`) that fires at midnight.

It sends alerts to a channel named `jee-reminders` (or falls back to `general`) when an exam is:
- 30 days away
- 15 days away
- 7 days away
- 3 days away
- 1 day away

---

## 📝 Updating Resources / Exam Dates

All data lives in `utils/exam_data.py`:

- **Add a new resource**: append to `RESOURCES["physics"]["optics"]` (or any subject/topic)
- **Update exam dates**: edit dates in `JEE_SCHEDULE`
- **Add a new topic**: add it to `TOPICS["physics"]` and `RESOURCES["physics"]`

---

## 🛠️ Extending the Bot

Want to add more features? Here's a quick guide:

```python
# Add a new cog: cogs/tracker.py
class Tracker(commands.Cog):
    @commands.command(name="track")
    async def track(self, ctx, subject: str):
        # log study session to MongoDB
        pass

async def setup(bot):
    await bot.add_cog(Tracker(bot))
```

Then register it in `bot.py`:
```python
await bot.load_extension("cogs.tracker")
```

---

## 📋 Command Reference

```
!notes                          → Show all subjects
!notes physics                  → All physics resources
!notes physics optics           → Optics notes/PDFs/playlists
!notes chemistry organic        → Organic chemistry resources
!notes maths calculus           → Calculus resources
!notes general                  → PYQs, mock tests, syllabus

!syllabus                       → Full syllabus overview
!syllabus physics               → Physics unit breakdown

!schedule                       → All JEE 2025 dates
!schedule main                  → JEE Main dates
!schedule advanced              → JEE Advanced date
!countdown                      → Days until next exam
!remind JEE Main                → Set personal reminder
!remind JEE Advanced            → Set personal reminder
!myreminders                    → View your reminders

!help                           → This command list
!ping                           → Check bot latency
```

---

Good luck with JEE 2025! 💪🔥
