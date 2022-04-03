import discord
from discord.ext import commands

class Mencionar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #mencionar o bot
    
    @commands.Cog.listener()
    async def on_message(self, message):             
            if message.content == '<@957084623060488302>':
                embed = discord.Embed(
                    title = "Mensagem de ajuda",
                    description = f"Olá, {message.author.mention} me chamo Mitsuy. Meu prefix padrão é `!` caso precise de ajuda, utilize o comando `!help`",
                    color = 0x0000ff
                )
                embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                await message.channel.send(embed=embed, delete_after=60)
                await message.delete()

def setup(bot):
    bot.add_cog(Mencionar(bot))