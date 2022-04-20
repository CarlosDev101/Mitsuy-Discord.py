import discord
from discord.ext import commands

class SeeChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # permitir que membros comuns vejam o chat
    
    @commands.command(name="Seeunlock", aliases=["Verchat", "seeunlock", "verchat"], help="Permitir que os membros vejam o canal")
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def seeunlock(self, ctx):
        embed = discord.Embed(
            title = "Acesso liberado",
            description = ctx.channel.mention + " Membros comuns agora podem ver mensagens!",
            color = 0x0000ff
        )
        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
        await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=True)
        await ctx.send(embed=embed)
        await ctx.message.delete()
    
    @seeunlock.error
    async def seeunlock_error(self, ctx, error):
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
    bot.add_cog(SeeChat(bot))