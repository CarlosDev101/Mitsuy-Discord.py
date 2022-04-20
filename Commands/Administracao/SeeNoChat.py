import discord
from discord.ext import commands

class SeeNoChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #impedir que membros comuns vejam o chat
    @commands.guild_only()
    @commands.command(name="Seelock", aliases=["ocultarchat", "seelock", "Ocultarchat"], help="Impedir que os membros comuns vejam o canal")
    @commands.has_permissions(manage_channels=True)
    async def seelock(self, ctx):
        embed = discord.Embed(
            title="Acesso Liberado",
            description = ctx.channel.mention + " Membros comuns não podem ver as mensagens!",
            color = 0x0000ff
        )
        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
        await ctx.send(embed=embed)
        await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=False)
        await ctx.message.delete()
    
    @seelock.error
    async def seelock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Acesso Negado",
                description= f"{ctx.author.mention} Você não tem permissão para usar este comando!",
                color = 0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed)
            await ctx.message.delete()

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='Parece que você esqueceu de algo...',
                description='Mencione na frente o canal.',
                color= 0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(SeeNoChat(bot))