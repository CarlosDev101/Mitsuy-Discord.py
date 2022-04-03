import discord
from discord.ext import commands

class AvatarMember(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #ver avatar do usuario
    
    @commands.command()
    @commands.guild_only()
    async def avatar(self, ctx, member: discord.Member = None):
        if not ctx.author.guild_permissions.manage_messages:
            embed = discord.Embed(
                title = "Acesso negado",
                color = 0x0000ff
            )
            embed.add_field(value = f"\n{ctx.author.mention} você não tem permissão para usar este comando")
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()
	
        else:
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
                title = "Eita... parece que você se esqueceu de algo",
                color = 0x0000ff
                )
            embed.add_field(value = f"\n{ctx.author.mention} por favor, mencione o úsuario na qual você quer ver a foto")
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(AvatarMember(bot))
    
