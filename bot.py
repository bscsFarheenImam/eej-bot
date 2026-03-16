import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
from datetime import datetime
import asyncio

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"✅ {bot.user} is online!")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="JEE aspirants grind 📚"
        )
    )
    check_reminders.start()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="❓ Unknown Command",
            description="Use `!help` to see all available commands.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="⚠️ Missing Argument",
            description=f"You're missing a required argument. Use `!help` for usage info.",
            color=discord.Color.orange()
        )
        await ctx.send(embed=embed)
    else:
        raise error


async def load_cogs():
    for cog in ["cogs.notes", "cogs.schedule", "cogs.help"]:
        await bot.load_extension(cog)
        print(f"  Loaded: {cog}")


@tasks.loop(hours=24)
async def check_reminders():
    """Daily reminder loop — fires exam alerts if an exam is within 30 days."""
    from utils.exam_data import JEE_SCHEDULE
    today = datetime.now()

    for guild in bot.guilds:
        # Try to find a channel named 'jee-reminders' or 'general'
        channel = discord.utils.get(guild.text_channels, name="jee-reminders") or \
                  discord.utils.get(guild.text_channels, name="general")
        if not channel:
            continue

        for exam in JEE_SCHEDULE:
            exam_date = exam["date"]
            days_left = (exam_date - today).days
            if days_left in [30, 15, 7, 3, 1]:
                embed = discord.Embed(
                    title=f"⏰ Exam Reminder — {exam['name']}",
                    description=f"**{days_left} day(s)** to go!\n\n📅 {exam_date.strftime('%d %B %Y')}\n\n{exam['note']}",
                    color=discord.Color.gold()
                )
                embed.set_footer(text="Stay consistent. You've got this! 💪")
                await channel.send(embed=embed)


async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
