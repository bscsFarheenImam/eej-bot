import discord
from discord.ext import commands
from datetime import datetime
from utils.exam_data import JEE_SCHEDULE
from utils.db import save_reminder, get_reminders_for_user


class Schedule(commands.Cog):
    """Exam schedule and reminder commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="schedule")
    async def schedule(self, ctx, exam_type: str = None):
        """
        Show upcoming JEE exam dates.
        Usage: !schedule | !schedule main | !schedule advanced
        """
        today = datetime.now()
        exams = JEE_SCHEDULE

        if exam_type:
            exam_type = exam_type.lower()
            exams = [e for e in JEE_SCHEDULE if e["type"].lower() == exam_type]
            if not exams:
                await ctx.send(f"❌ No exams found for `{exam_type}`. Try `!schedule main` or `!schedule advanced`.")
                return

        embed = discord.Embed(
            title="📅 JEE 2025 Exam Schedule",
            description="Stay ahead of every deadline. React with 🔔 to set a reminder for an exam.",
            color=discord.Color.blue()
        )

        for i, exam in enumerate(exams, 1):
            days_left = (exam["date"] - today).days
            if days_left < 0:
                status = "✅ Completed"
                color_bar = "🔘"
            elif days_left == 0:
                status = "🔴 TODAY"
                color_bar = "🔴"
            elif days_left <= 7:
                status = f"🔴 {days_left}d left — SOON!"
                color_bar = "🔴"
            elif days_left <= 30:
                status = f"🟡 {days_left} days left"
                color_bar = "🟡"
            else:
                status = f"🟢 {days_left} days left"
                color_bar = "🟢"

            subjects_str = " • ".join(exam["subjects"])

            embed.add_field(
                name=f"{color_bar} {exam['name']}",
                value=(
                    f"📅 **{exam['date'].strftime('%d %B %Y')}**\n"
                    f"⏳ {status}\n"
                    f"📚 {subjects_str}\n"
                    f"ℹ️ _{exam['note']}_\n"
                    f"🌐 [Official Site]({exam['link']})"
                ),
                inline=False
            )

        embed.set_footer(text="Use !remind <exam_name> to get a personal DM reminder • !countdown for next exam")
        embed.timestamp = discord.utils.utcnow()
        await ctx.send(embed=embed)

    @commands.command(name="countdown")
    async def countdown(self, ctx):
        """Show countdown to the next upcoming JEE exam."""
        today = datetime.now()
        upcoming = [e for e in JEE_SCHEDULE if (e["date"] - today).days >= 0]

        if not upcoming:
            embed = discord.Embed(
                title="🏁 All JEE 2025 exams are done!",
                description="Results and counselling season ahead. Good luck! 🎉",
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)
            return

        next_exam = min(upcoming, key=lambda e: e["date"])
        days_left = (next_exam["date"] - today).days
        hours_left = int(((next_exam["date"] - today).total_seconds() % 86400) / 3600)

        # Progress bar (30 days = full bar)
        bar_length = 20
        max_days = 30
        filled = max(0, bar_length - int((days_left / max_days) * bar_length))
        bar = "🟥" * min(filled, bar_length) + "⬜" * (bar_length - min(filled, bar_length))

        embed = discord.Embed(
            title=f"⏳ Next Exam: {next_exam['name']}",
            color=discord.Color.red() if days_left <= 7 else discord.Color.orange() if days_left <= 30 else discord.Color.green()
        )
        embed.add_field(name="📅 Date", value=next_exam["date"].strftime("%d %B %Y"), inline=True)
        embed.add_field(name="⏰ Time Left", value=f"**{days_left}d {hours_left}h**", inline=True)
        embed.add_field(name="📊 Urgency Meter", value=bar, inline=False)
        embed.add_field(name="ℹ️ Note", value=next_exam["note"], inline=False)

        if days_left <= 7:
            embed.set_footer(text="🔥 Final stretch! Revise formulas, attempt mocks, sleep well.")
        elif days_left <= 30:
            embed.set_footer(text="📝 One month to go — complete syllabus, start mock tests.")
        else:
            embed.set_footer(text="✅ You have time — stay consistent with your daily targets.")

        await ctx.send(embed=embed)

    @commands.command(name="remind")
    async def remind(self, ctx, *, exam_name: str = None):
        """
        Set a personal DM reminder for a JEE exam.
        Usage: !remind JEE Main | !remind JEE Advanced
        """
        if exam_name is None:
            await ctx.send("❌ Usage: `!remind JEE Main` or `!remind JEE Advanced`")
            return

        exam_name_lower = exam_name.lower()
        matched = None
        for exam in JEE_SCHEDULE:
            if exam_name_lower in exam["name"].lower() or exam_name_lower in exam["type"].lower():
                matched = exam
                break

        if not matched:
            names = "\n".join(f"• `{e['name']}`" for e in JEE_SCHEDULE)
            await ctx.send(f"❌ Couldn't find that exam. Available exams:\n{names}")
            return

        today = datetime.now()
        days_left = (matched["date"] - today).days

        if days_left < 0:
            await ctx.send(f"⚠️ **{matched['name']}** has already passed.")
            return

        # Save reminder to DB
        await save_reminder(
            guild_id=ctx.guild.id,
            channel_id=ctx.channel.id,
            user_id=ctx.author.id,
            exam_name=matched["name"],
            remind_date=matched["date"]
        )

        embed = discord.Embed(
            title="🔔 Reminder Set!",
            description=(
                f"You'll get reminders **30, 15, 7, 3, and 1 day(s)** before:\n\n"
                f"📌 **{matched['name']}**\n"
                f"📅 {matched['date'].strftime('%d %B %Y')}\n"
                f"⏳ {days_left} days away"
            ),
            color=discord.Color.green()
        )
        embed.set_footer(text="Reminders are sent to this channel. Stay consistent! 💪")
        await ctx.send(embed=embed)

        # DM confirmation
        try:
            await ctx.author.send(
                embed=discord.Embed(
                    title="✅ Reminder Confirmed",
                    description=f"You're set for **{matched['name']}** on {matched['date'].strftime('%d %B %Y')}!",
                    color=discord.Color.green()
                )
            )
        except discord.Forbidden:
            pass  # User has DMs disabled

    @commands.command(name="myreminders")
    async def myreminders(self, ctx):
        """See all your active exam reminders. Usage: !myreminders"""
        reminders = await get_reminders_for_user(ctx.author.id)

        if not reminders:
            await ctx.send("📭 You have no active reminders. Use `!remind <exam>` to set one.")
            return

        embed = discord.Embed(
            title=f"🔔 {ctx.author.display_name}'s Reminders",
            color=discord.Color.blue()
        )
        for r in reminders:
            days_left = (r["remind_date"] - datetime.now()).days
            embed.add_field(
                name=f"📌 {r['exam_name']}",
                value=f"📅 {r['remind_date'].strftime('%d %B %Y')} — {max(0, days_left)}d left",
                inline=False
            )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Schedule(bot))
