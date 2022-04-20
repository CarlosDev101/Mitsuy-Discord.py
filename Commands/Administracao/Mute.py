import discord, datetime
from discord.ext import commands

class Mute(commands.Cog):
    def __inti__(self, bot):
        self.bot = bot

    @commands.guild_only() 
    @commands.has_permissions(manage_roles=True)
    @commands.command(name="Mute", aliases=["mute"])
    async def mute(self, ctx, member: discord.Member, *, reason: str = None):
        muted = discord.utils.get(ctx.guild.roles, name='Mutado')
        await member.add_roles(muted)
        embed = discord.Embed(
            title=f"{ctx.member.name} Mutado",
            description=f"Espero que na proxima vez você diga coisas boas!\n\n**ADM:**{ctx.author.mention}\n**Membro:**{ctx.member.mention}\n**Motivo:**{reason}",
            color=0x0000ff
        )
        embed.timestamp= datetime.datetime.utcnow()
        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
        await ctx.member.mention.send(embed=embed)
        await ctx.author.send(embed=embed)
        await ctx.message.delete()

    @mute.error
    async def mute_error(self, ctx, error):
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
    bot.add_cog(Mute(bot))