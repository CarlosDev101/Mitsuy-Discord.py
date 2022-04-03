import discord
from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #limpar o chat
    
    @commands.command(aliases=["limpar"])
    @commands.guild_only()
    async def clear(self, ctx, amount=11):
        if not ctx.author.guild_permissions.manage_messages:
            embed = discord.Embed(
                title = "Acesso negado",
                color = 0x0000ff
            )
            embed.add_field(value = f"\n{ctx.author.mention} você não tem permissão para usar este comando")
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()
        
        ammount = amount + 1
        if amount > 1000000:
            embed = discord.Embed(
                title = "Acesso negado",
                color = 0x0000ff
            )
            embed.add_field(value = f"\n{ctx.author.mention} você não pode excluir mais de 1 milhão de mensagens")	
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()
        
        else:
            await ctx.channel.purge(limit=amount)
            embed = discord.Embed(
                title = "Acesso liberado",
                color = 0x0000ff
            )
            embed.add_field(value = f"\n{ctx.author.mention} mensagens apagadas!")
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)

def setup(bot):
    bot.add_cog(Clear(bot))