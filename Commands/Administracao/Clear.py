import discord
from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #limpar o chat

    @commands.guild_only() 
    @commands.has_permissions(manage_channels=True)
    @commands.command(name="clear", aliases=["limpar", "Clear", "Limpar"], help="Limpa o chat")
    async def clear(self, ctx, amount= 11):  
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
        
    @clear.error
    async def clear_error(self, ctx, error):
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
                description='Digite o quanto de mensagem você quer deletar.',
                color= 0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(Clear(bot))