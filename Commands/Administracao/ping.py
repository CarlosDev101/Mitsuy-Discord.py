import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #sistema de ping
    
    @commands.command(aliases = ["latencia"])
    async def ping(self, ctx):
        latencia = round(self.bot.latency * 1000, 1)
        embed = discord.Embed(
            title = "Informação de Latência",
            description = f"{ctx.author.mention} você tem {latencia} ms",
            color = 0x0000ff
        )
        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
        await ctx.send(embed=embed, delete_after=60)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Ping(bot))