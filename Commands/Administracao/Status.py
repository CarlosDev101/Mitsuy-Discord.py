import discord
from discord.ext import commands, tasks
from itertools import cycle

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #status do bot
     
    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        print(self.bot.user.name + "estou online")
    
    
    @tasks.loop(seconds=60)
    async def change_status(self):
        everything = list()
        total = sum(everything)
        status = cycle(["@πΆπππππ  πΈππ’ππππ#8870 ", f'Estou em {len(self.bot.guilds)} servidores!', 'Meu prefix padrΓ£o Γ©      !', 'Estou em desenvolvimento!'])
        await self.bot.change_presence(activity=discord.Game(next(status)))

def setup(bot):
    bot.add_cog(Status(bot))