import decouple, os
from discord.ext import commands

bot = commands.Bot("!")
bot.remove_command("help")


def load_cogs(bot):

    for comandos in os.listdir("Commands"):
        if comandos.endswith(".py"):
            cog2 = comandos[:-3]
            bot.load_extension(f"Commands.{cog2}")

    for commands in os.listdir("Commands/Administracao"):
        if commands.endswith(".py"):
            cog3 = commands[:-3]
            bot.load_extension(f"Commands.Administracao.{cog3}")
    
    
    for commands in os.listdir("Commands/Leveling"):
        if commands.endswith(".py"):
            cog3 = commands[:-3]
            bot.load_extension(f"Commands.Leveling.{cog3}")

load_cogs(bot)            

TOKEN = decouple.config("token_secret")
bot.run(TOKEN)
