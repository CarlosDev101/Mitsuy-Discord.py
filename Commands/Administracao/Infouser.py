import discord
from discord.ext import commands

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    @commands.command(name="UserInfo", aliases=["userinfo", "InfoUser", "infouser"], help="Ver as informações sobre o membro")
    async def userinfo(self, ctx, member: discord.Member):
        roles = [role for role in member.roles]
        embed = discord.Embed(
            title="Informações do usuário",
            color= 0x0000ff
        )
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Solicitado por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="**ID**", value=member.id)
        embed.add_field(name="**Nome do membro**:", value= member.display_name)
        embed.add_field(name="**Conta criada**:", value= member.created_at.strftime("%d/%m/%Y as %H:%M"))
        embed.add_field(name="**Entrou no servidor**:", value= member.joined_at.strftime("%d/%m/%Y as %H:%M"))
        embed.add_field(name=f"**Cargo**: ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=60)
    
    @userinfo.error
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
                description='Mencione o usuario para você obter as informações dele.',
                color= 0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(Information(bot))