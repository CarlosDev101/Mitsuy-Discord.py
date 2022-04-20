import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #sistema de ping
    
    @commands.command(name="Ping", aliases = ["latencia", "Latencia", "ping"], help="Ver a latencia")
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
    
    @ping.error
    async def ping_error(self, error, ctx):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='Parece que você esqueceu de algo...',
                description='Mencione o usuario para você obter a latencia dele.',
                color= 0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(Ping(bot))