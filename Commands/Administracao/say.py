import discord, datetime
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    #mandar o bot falar algo

    @commands.command(aliases=["falar"])
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def say(self, ctx, *, msg):
            tempo = datetime.datetime.now() #pegar o tempo de agora
            tempo = tempo.strftime("%d/%m/%Y-%H:%M:%S") #formatando a data/horario
            embed = discord.Embed(
                title = "Aviso importatente",
                color = 0x0000ff,
                description = f"{msg}"
            )

            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            embed.set_footer(text= "Feito por: " + ctx.author.name + " ás: " + tempo, icon_url = ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(Say(bot))
