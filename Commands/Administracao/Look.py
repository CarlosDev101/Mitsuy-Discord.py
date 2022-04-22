import discord
from discord.ext import commands

class Lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #trancar o chat
    
    @commands.guild_only()
    @commands.command(name="Lock", aliases=["Trancar", "trancar", "lock"], help="Tranca o canal de texto")
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        embed = discord.Embed(
            title = "Acesso liberado",
            description = ctx.channel.mention + " agora está trancado!",
            color = 0x0000ff
        )
        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()
    
    @lock.error
    async def lock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Acesso negado",
                color = 0x0000ff
            )
            embed.add_field(value = f"\n{ctx.author.mention} você não tem permissão para usar este comando")
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()
        
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='Parece que você esqueceu de algo...',
                description='Mencione o canal para você trancar ele.',
                color= 0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(Lock(bot))