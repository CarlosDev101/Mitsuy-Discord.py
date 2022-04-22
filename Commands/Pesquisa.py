import discord, random
from time import sleep
from googleapiclient.discovery import build
from discord.ext import commands

class Pesquisa(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command(name="Pesquisar", aliases=["pesquisar", "search", "Scearch"])
    async def imagem(self, ctx, *, search):
        api_key = "YOUR_KEY"
        ran = random.randint(0, 9)
        resource = build("customsearch", "v1", developerKey=api_key).cse()
        result = resource.list(q=f"{search}", cx="2601e91526cbf388d", searchType="image").execute()
        url = result["items"][ran]["link"]
        embed = discord.Embed(title=f"Sua imagem {ctx.author.name} ({search.title()})", coulor=0x0000ff)
        embed.set_image(url=url)
        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = embed, delete_after=60)
        sleep(60)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Pesquisa(bot))
