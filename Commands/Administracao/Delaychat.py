import discord
from discord.ext import commands

class Delaychat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    @commands.command(name="Delay", aliases=["delay", "Lento", "lento"])
    async def lento(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        if seconds > 0:
            embed = discord.Embed(
                title="Delay aplicado",
                description=f"O canal {ctx.channel.mention} está com {seconds} segundos de delay.",
                color=0x0000ff
            )
            await ctx.reply(embed=embed)

        if seconds == 0:
            embed = discord.Embed(
                title="Delay aplicado",
                description=f"O canal {ctx.channel.mention} saiu do delay.",
                color=0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.reply(embed=embed)

    @lento.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='Parece que você esqueceu de algo...',
                description='Mencione o canal e informe o tempo de delay.',
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
    bot.add_cog(Delaychat(bot))