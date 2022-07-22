import discord, requests
from discord.ext import commands

class IA(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Ia", aliases=["ia","IA", "iA", "AI", "aI", "Ai"])
    @commands.guild_only()
    async def ia(self, ctx, *, msg):
        bot = requests.get(f"https://api.simsimi.net/v2/?text={msg}&lc=pt&cf=false").json()
        await ctx.reply(bot["success"])
    
    @ia.error
    async def IA_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Parece que você esqueceu de algo...",
                description=f"""{ctx.author.mention} voce precisa digitar uma mensagem para conversar com a IA*
                """,
                color=0x0000ff
            )
            await ctx.message.delete()
            await ctx.send(embed=embed, delete_after=30)

def setup(bot):
    bot.add_cog(IA(bot))
