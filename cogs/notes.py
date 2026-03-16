import discord
from discord.ext import commands
from utils.exam_data import RESOURCES, SUBJECTS, TOPICS


class Notes(commands.Cog):
    """Resource sharing commands for JEE preparation."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="notes")
    async def notes(self, ctx, subject: str = None, topic: str = None):
        """
        Fetch curated study resources.

        Usage:
          !notes                        — show all subjects
          !notes physics                — all physics resources
          !notes physics optics         — optics-specific resources
          !notes chemistry organic
          !notes maths calculus
        """
        # ── No args: show subject menu ──
        if subject is None:
            embed = discord.Embed(
                title="📚 JEE Study Resources",
                description="Use `!notes <subject>` or `!notes <subject> <topic>` to get resources.",
                color=discord.Color.blue()
            )
            for subj in SUBJECTS:
                topics_list = ", ".join(f"`{t}`" for t in TOPICS[subj] if t != "general")
                embed.add_field(
                    name=f"📖 {subj.capitalize()}",
                    value=f"Topics: {topics_list}\nUse: `!notes {subj}`",
                    inline=False
                )
            embed.add_field(
                name="🗂️ General",
                value="PYQs, Mock Tests, Syllabus\nUse: `!notes general`",
                inline=False
            )
            embed.set_footer(text="Tip: !notes physics optics → gets optics-specific notes")
            await ctx.send(embed=embed)
            return

        subject = subject.lower()

        # ── General resources ──
        if subject == "general":
            embed = discord.Embed(
                title="🗂️ General JEE Resources",
                description="PYQs, mock tests, and official links.",
                color=discord.Color.green()
            )
            for res in RESOURCES["general"]:
                embed.add_field(
                    name=f"{res['type']} {res['title']}",
                    value=f"[Open Link]({res['url']})",
                    inline=False
                )
            embed.set_footer(text="Use !schedule to see upcoming exam dates.")
            await ctx.send(embed=embed)
            return

        # ── Validate subject ──
        if subject not in SUBJECTS:
            embed = discord.Embed(
                title="❌ Unknown Subject",
                description=f"Available subjects: {', '.join(f'`{s}`' for s in SUBJECTS)} or `general`",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return

        # ── Topic-specific ──
        if topic:
            topic = topic.lower()
            valid_topics = TOPICS[subject]
            if topic not in valid_topics:
                embed = discord.Embed(
                    title=f"❌ Unknown Topic for {subject.capitalize()}",
                    description=f"Valid topics: {', '.join(f'`{t}`' for t in valid_topics)}",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embed)
                return

            resources = RESOURCES[subject].get(topic, [])
            embed = discord.Embed(
                title=f"📖 {subject.capitalize()} — {topic.capitalize()} Resources",
                description=f"Curated notes, PDFs & playlists for **{topic}**.",
                color=discord.Color.teal()
            )
        else:
            # ── All topics for subject ──
            all_resources = []
            for t, res_list in RESOURCES[subject].items():
                all_resources.extend(res_list)
            resources = all_resources

            embed = discord.Embed(
                title=f"📖 {subject.capitalize()} — All Resources",
                description=f"All curated resources for **{subject}**. Use `!notes {subject} <topic>` to filter.",
                color=discord.Color.teal()
            )

        if not resources:
            embed.description = "No resources found for this topic yet. Check back soon!"
        else:
            for res in resources[:10]:  # Cap at 10 to avoid embed overflow
                embed.add_field(
                    name=f"{res['type']} {res['title']}",
                    value=f"[Open Link]({res['url']})",
                    inline=False
                )

        embed.set_footer(text="All resources are community-curated. Report broken links to admins.")
        await ctx.send(embed=embed)

    @commands.command(name="syllabus")
    async def syllabus(self, ctx, subject: str = None):
        """
        Show the JEE syllabus for a subject.
        Usage: !syllabus | !syllabus physics | !syllabus chemistry | !syllabus maths
        """
        syllabus_data = {
            "physics": [
                "📐 Mechanics — Laws of Motion, Work-Energy, Rotational Motion",
                "🌡️ Thermodynamics — Heat, KTG, Thermal Expansion",
                "🔊 Waves & Oscillations — SHM, Sound, Standing Waves",
                "⚡ Electrostatics & Magnetism — Fields, Capacitors, EM Induction",
                "💡 Optics — Ray Optics, Wave Optics, Interference",
                "☢️ Modern Physics — Photoelectric Effect, Nuclear Physics",
            ],
            "chemistry": [
                "🧪 Physical Chemistry — Mole Concept, Equilibrium, Electrochemistry",
                "⚗️ Inorganic Chemistry — Periodic Table, Bonding, p/d/f Block",
                "🔬 Organic Chemistry — Hydrocarbons, Reactions, Biomolecules",
            ],
            "maths": [
                "📊 Algebra — Complex Numbers, Quadratics, Sequences",
                "📐 Trigonometry — Identities, Inverse Functions, Properties",
                "📈 Calculus — Limits, Derivatives, Integration, Differential Equations",
                "🗺️ Coordinate Geometry — Straight Lines, Conic Sections",
                "🎲 Probability & Statistics — Permutations, Bayes' Theorem",
                "🔢 Matrices & Determinants, 3D Geometry, Vectors",
            ]
        }

        if subject is None:
            embed = discord.Embed(
                title="📋 JEE Syllabus Overview",
                description="Use `!syllabus <subject>` for a detailed breakdown.",
                color=discord.Color.purple()
            )
            for subj, topics in syllabus_data.items():
                embed.add_field(
                    name=f"📚 {subj.capitalize()} ({len(topics)} units)",
                    value="\n".join(topics[:3]) + "\n_...and more_",
                    inline=False
                )
        else:
            subject = subject.lower()
            if subject not in syllabus_data:
                await ctx.send(f"❌ Unknown subject. Try: `!syllabus physics`, `!syllabus chemistry`, or `!syllabus maths`")
                return
            embed = discord.Embed(
                title=f"📋 JEE {subject.capitalize()} Syllabus",
                color=discord.Color.purple()
            )
            for unit in syllabus_data[subject]:
                embed.add_field(name=unit, value="\u200b", inline=False)

        embed.set_footer(text="Based on NTA JEE 2025 official syllabus.")
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Notes(bot))
