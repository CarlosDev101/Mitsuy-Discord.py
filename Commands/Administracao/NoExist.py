import discord
from discord.ext import commands

class NoExist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #comando nao existe
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                title = "Comando não existe",
                discription = f"{ctx.author.mention} este comando não existe! Caso precise de ajuda, utilize o comando `!help`",
                color = 0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.message.delete()
            await ctx.send(embed=embed, delete_after=60)
    
def setup(bot):
    bot.add_cog(NoExist(bot))