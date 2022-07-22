import discord
from discord.ext import commands

class AvatarMember(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #ver avatar do usuario
    
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    @commands.command(name="Avatar", aliases=["Seeavatar", "seeavatar", "avatar"], help="Ver o avatar do membro")

    async def avatar(self, ctx, member: discord.Member = None):
            embed = discord.Embed(
                title = f"Aqui esta o avatar do {member.name}",
                color = 0x0000ff
            )
            embed.set_image(url=member.avatar_url)
            await ctx.message.delete()
            await ctx.send(embed=embed, delete_after=60)
        
    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='Parece que você esqueceu de algo...',
                description='Mencione na frente o usuario.',
                color= 0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()
            
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Acesso Negado",
                description= f"{ctx.author.mention} Você não tem permissão para usar este comando!",
                color = 0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed)
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(AvatarMember(bot))
    
