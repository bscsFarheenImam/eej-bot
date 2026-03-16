import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        """Show all bot commands."""
        embed = discord.Embed(
            title="📚 JEE Bot — Command Reference",
            description="Your all-in-one JEE prep companion. Here's what I can do:",
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="📖 Notes & Resources",
            value=(
                "`!notes` — Browse all subjects\n"
                "`!notes <subject>` — All resources for a subject\n"
                "`!notes <subject> <topic>` — Topic-specific notes\n"
                "`!syllabus` — Full JEE syllabus overview\n"
                "`!syllabus <subject>` — Detailed unit-wise syllabus\n\n"
                "_Examples:_ `!notes physics optics` | `!notes maths calculus`"
            ),
            inline=False
        )

        embed.add_field(
            name="📅 Exam Schedule & Reminders",
            value=(
                "`!schedule` — All upcoming JEE exam dates\n"
                "`!schedule main` — JEE Main dates only\n"
                "`!schedule advanced` — JEE Advanced date\n"
                "`!countdown` — Days left for next exam\n"
                "`!remind <exam>` — Set personal reminders\n"
                "`!myreminders` — View your active reminders\n\n"
                "_Example:_ `!remind JEE Advanced`"
            ),
            inline=False
        )

        embed.add_field(
            name="ℹ️ Tips",
            value=(
                "• Commands are case-insensitive\n"
                "• Reminders fire at 30, 15, 7, 3, and 1 day(s) before an exam\n"
                "• New resources added regularly — use `!notes` to check"
            ),
            inline=False
        )

        embed.set_footer(text="Built for JEE aspirants | Stay consistent 💪")
        embed.set_thumbnail(url="https://i.imgur.com/placeholder_jee.png")
        await ctx.send(embed=embed)

    @commands.command(name="ping")
    async def ping(self, ctx):
        """Check bot latency."""
        latency = round(self.bot.latency * 1000)
        color = discord.Color.green() if latency < 100 else discord.Color.orange() if latency < 200 else discord.Color.red()
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Latency: **{latency}ms**",
            color=color
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))
