import discord
from discord.ext import commands

class CriarCargo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #CRIAR O CARGO MUTADO AO ENTRAR NO SERVER
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        cargo = discord.utils.get(guild.roles, name='Mutado 😶')
        if cargo == None:
            perms = discord.Permissions(send_messages=False, read_messages=True)
            await guild.create_role(name="Mutado 😶", permissions=perms)
        
        else:
	        pass

def setup(bot):
    bot.add_cog(CriarCargo(bot))