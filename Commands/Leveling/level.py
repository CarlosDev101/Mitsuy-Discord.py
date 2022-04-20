import discord, json
from discord.ext import commands

class Leveling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.Cog.listener()
    async def on_message(self, message):
        with open(f"Commands/Leveling/users.json", "r+", encoding="utf8") as f:
            user = json.load(f)
        
        try:
            with open("Commands/Leveling/users.json", "w+", encoding="utf8") as f:
                user[str(message.author.id)]["exp"] = user[str(message.author.id)]["exp"] + 1
                lvl_start = user[str(message.author.id)]["level"]
                lvl_end = user[str(message.author.id)]["exp"] ** (1.5/4)
                if lvl_start < lvl_end:
                    user[str(message.author.id)]["level"] = user[str(message.author.id)]["level"] + 1
                    lvl = user[str(message.author.id)]["level"]
                    embed = discord.Embed(
                        title = "Subiu de nivel",
                        description = f"{message.author.mention} você subiu para o nivel {lvl}",
                        color = 0x0000ff

                    )
                    embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url) 
                    await message.channel.send(embed=embed)
                    json.dump(user, f, sort_keys=True, indent=4, ensure_ascii=False)
                    return
                
                json.dump(user, f, sort_keys=True, indent=4, ensure_ascii=False)	
        
        except:
            with open("Commands/Leveling/users.json", "w+", encoding="utf8") as f:
                user = { }
                user[str(message.author.id)] = {}
                user[str(message.author.id)]["level"] = 0
                user[str(message.author.id)]["exp"] = 0
                json.dump(user, f, sort_keys=True, indent=4, ensure_ascii=False)

def setup(bot):
    bot.add_cog(Leveling(bot))