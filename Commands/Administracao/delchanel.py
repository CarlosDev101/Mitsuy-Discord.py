import discord
from discord.ext import commands

class DelChanell(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['deletarcanal'])
    @commands.cooldown(1, 2, commands.BucketType.guild)
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def delcanal(self, ctx, *, channel: discord.TextChannel):
        embed = discord.Embed(
            title = "Acesso liberado!",
            description = f"Canal {channel} foi deletado",
            color = 0x0000ff
        )
        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
        if ctx.author.guild_permissions.manage_channels:
            await ctx.send(embed=embed)
            await ctx.message.delete()
            await channel.delete()
    
    @delcanal.error
    async def delcanal_error(self, ctx, error):
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
                description='Escreva o nome/id do canal de texto que você quer deletar.',
                color= 0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(DelChanell(bot))