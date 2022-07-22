import discord, datetime
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    #mandar o bot falar algo

    @commands.command(name="say", aliases=["Say", "Falar", "falar"], help="Manda uma mensagem de texto através do bot")
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

    @say.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
            title='Acesso negado',
            description='Ops, parece que você não tem permissão para usar este comando!',
            color= 0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()
        
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='Parece que você esqueceu de algo...',
                description='Digite na frente a mensagem na qual voce queira enviar.',
                color= 0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()         

def setup(bot):
    bot.add_cog(Say(bot))
