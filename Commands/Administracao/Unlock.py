import discord
from discord.ext import commands

class Unlock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #destracancar o chat para os outros falarem
    
    @commands.command(aliases=['destrancar'])
    @commands.cooldown(1, 2, commands.BucketType.guild)
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def unlock(self, ctx):
        embed = discord.Embed(
            title = "Acesso liberado",
            description = ctx.channel.mention + " foi destrancado!",
            color = 0x0000ff
        )
        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)    
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Acesso negado",
                color = 0x0000ff
            )
            embed.add_field(value = f"\n{ctx.author.mention} você não tem permissão para usar este comando")
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(Unlock(bot))