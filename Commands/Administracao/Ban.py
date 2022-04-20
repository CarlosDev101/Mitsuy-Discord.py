import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.guild_only()
    @commands.command(name="Ban", aliases=["ban"], help="Banir o usuario")
    @commands.has_permissions(manage_channels=True)
    async def banimento(self, ctx, member: discord.Member, *, reason=None):        
        await ctx.guild.ban(user=member, reason=reason)
        embed = discord.Embed(
            title=f"{ctx.member.mention} banido",
            description= f"**ADM**: {ctx.author.mention}\n\n**MEMBRO**: {member.mention}\n\n**MOTIVO**: {reason}",
            color=0x0000ff
        )
        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
        await ctx.member.mention.send(embed=embed)
        await ctx.author.send(embed=embed)
        await ctx.message.delete()

    @banimento.error
    async def kick_error(self, ctx, error):
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
    bot.add_cog(Ban(bot))