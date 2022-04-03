import discord
from discord.ext import commands

class SeeNoChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #impedir que membros comuns vejam o chat
    @commands.command(aliases=["naochat"])
    @commands.cooldown(1, 2, commands.BucketType.guild)
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
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

def setup(bot):
    bot.add_cog(SeeNoChat(bot))