import discord
from translate import Translator
from discord.ext import commands

class Traduzir(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="Translate", aliases=["traduzir", "Traduzir", "translate"])
    @commands.guild_only()
    async def translate(self, ctx, fr, to, *, message):
        autor = ctx.author
        s = Translator(from_lang="{}".format(fr),
                   to_lang="{}".format(to))
        res = s.translate(message)
        await ctx.reply(f'{res}')
    
    @translate.error
    async def translate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Parece que você esqueceu de algo...",
                description=f"""{ctx.author.mention} você precisa digitar o idioma na qual voce escreveu, para qual idioma você quer traduzir e por fim sua mensagem
                Exeplo: *en pt Good Morning*
                """,
                color=0x0000ff
            )
            await ctx.message.delete()
            await ctx.send(embed=embed, delete_after=30)

def setup(bot):
    bot.add_cog(Traduzir(bot))
