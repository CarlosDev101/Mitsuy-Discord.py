import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="Help", alisases=['ajuda', "Ajuda"], help="Comando onde contem os comandos do bot")
    async def Help(self, ctx):
        embed = discord.Embed(
                    title='Menu de ajuda',
                    description=f"""Olá {ctx.author.mention}, reaja algum dos emojis abaixo para você ver a lista de comandos!
                    \nVocê vai receber na sua DM a lista de comandos. Para isso, certifique-se se sua DM esteja aberta.

                    👮🏼‍♂️  **Administrção**
                    🎮 **Jogos**
                    🎧 **Música**

                    \n[Instagram do dono](https://www.instagram.com/carlosdev10/)
                    \n[Servidor para suporte](https://discord.gg/9TcEt3bF)
                    """
        )
        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
        resposta = await ctx.reply(embed=embed, delete_after=60)
        await resposta.add_reaction("👮🏼‍♂️")
        await resposta.add_reaction("🎮")
        await resposta.add_reaction("🎧")
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, message):
        while True:
            if reaction.emoji == self.bot.user:
                pass
            if reaction.emoji == "👮🏼‍♂️":
                embed = discord.Embed(
                        title=f'Comandos da Mitsuy [pág 1/2]',
                        colour= 0x0000ff,
                        description ="""Olá, muito obrigado por estar utilizando o bot Mitsuy. 
                        \n**Avatar** - Vizualizar a foto de perfil do membro
                        \n**Clear** - Apaga as mensagens do servidor
                        \n**Createchannel** - Cria um canal de texto
                        \n**Delchannel** - Deleta canal de texto
                        \n**Help** - Ver os comandos do bot
                        \n**Loock** - Tranca o canal de texto
                        \n**Ping** - Vê a latencia
                        \n**Say** - Manda uma mensagem de texto através do bot
                        \n**Seeunlock** - Permitir que os membros vejam o canal
                        \n**Seelock** - Impedir que os membros comuns vejam o canal
                        \n**Traduzir** - Traduz uma mensagem para outro idioma
                        \n**Delay** - Coloca um delay no canal de texto
                        \n**Ban** - Vai banir um membro
                        \n**Unban** - Vai desbanir um membro
                        \n**Kick** - Expulsa um membro do servidor
                        \n**Mute** - Silencia um membro
                        \n**Unmute** - Tira o membro do mute
                        \n[Instagram do dono](https://www.instagram.com/carlosdev10/)
                        \n[Servidor para suporte](https://discord.gg/9TcEt3bF)
                        """
                )
                embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                resposta = await message.send(embed=embed, delete_after=60)
                await resposta.add_reaction("⏩")
                
                if reaction.emoji == "⏩":
                    embed = discord.Embed(
                        title=f'Comandos da Mitsuy [pág 2/2]',
                        colour= 0x0000ff,
                        description ="""Olá, muito obrigado por estar utilizando o bot Mitsuy. 
                        \n**Seelock** - Impedir que os membros comuns vejam o canal
                        \n**Traduzir** - Traduz uma mensagem para outro idioma
                        \n**Delay** - Coloca um delay no canal de texto
                        \n**Ban** - Vai banir um membro
                        \n**Unban** - Vai desbanir um membro
                        \n**Kick** - Expulsa um membro do servidor
                        \n**Mute** - Silencia um membro
                        \n**Unmute** - Tira o membro do mute
                        \n[Instagram do dono](https://www.instagram.com/carlosdev10/)
                        \n[Servidor para suporte](https://discord.gg/9TcEt3bF)
                        """
                    )
                    embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                    resposta = await message.send(embed=embed, delete_after=60)
                    break

            elif reaction.emoji == "🎮":
                embed = discord.Embed(
                        title=f'Comandos da Mitsuy',
                        colour= 0x0000ff,
                        description ="""Olá, muito obrigado por estar utilizando o bot Mitsuy.
                        \n**Tictac** - Jogue o jogo da velha (Necessário dois jogadores)
                        \n[Instagram do dono](https://www.instagram.com/carlosdev10/)
                        \n[Servidor para suporte](https://discord.gg/9TcEt3bF)
                        """
                )
                embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                resposta = await message.send(embed=embed, delete_after=60)
                break

            elif reaction.emoji == "🎧":
                embed = discord.Embed(
                        title=f'Comandos da Mitsuy',
                        colour= 0x0000ff,
                        description ="""Olá, muito obrigado por estar utilizando o bot Mitsuy.
                        \n**Play** - Toca uma música
                        \n**Queue** - Mostra as atuais músicas da fila
                        \n**Skip** - Pula a atual música que está tocando
                        \n**Pesquisar** - Pesquisa uma foto no google
                        \n[Instagram do dono](https://www.instagram.com/carlosdev10/)
                        \n[Servidor para suporte](https://discord.gg/9TcEt3bF)
                        """
                )
                embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                resposta = await message.send(embed=embed, delete_after=60)
                break

def setup(bot):
    bot.add_cog(Help(bot))
