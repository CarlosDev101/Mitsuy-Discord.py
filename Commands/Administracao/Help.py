import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="Help", alisases=['ajuda', "Ajuda"], help="Comando onde contem os comandos do bot")
    async def Help(self, ctx):
        embed = discord.Embed(
                    title=f'Comandos da Mitsuy [pág 1/3]',
                    colour= 0x0000ff,
                    description ="""Olá, muito obrigado por estar utilizando o bot Mitsuy. 
                    \n**Avatar** - Vizualizar a foto de perfil do membro
                    \n**Clear** - Apaga as mensagens do servidor
                    \n**Createchannel** - Cria um canal de texto
                    \n**Delchannel** - Deletar canal de texto
                    \n**Help** - Ver os comandos do bot
                    \n**Loock** - Tranca o canal de texto
                    \n**Ping** - Ver a latencia
                    \n**Say** - Manda uma mensagem de texto através do bot
                    \n**eeunlock** - Permitir que os membros vejam o canal
                    \n**Seelock** - Impedir que os membros comuns vejam o canal
                    \n**Traduzir** - Traduz uma mensagem para outro idioma
                    \n[Instagram do dono](https://www.instagram.com/carlosdev10/)
                    \n[Servidor para suporte](https://discord.gg/9TcEt3bF)
                    """
        )
        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
        resposta = await ctx.reply(embed=embed, delete_after=60)
        await resposta.add_reaction("1️⃣")
        await resposta.add_reaction("2️⃣")
        await resposta.add_reaction("3️⃣")
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, message):
        while True:
            if reaction.emoji == self.bot.user:
                pass
            if reaction.emoji == "1️⃣":
                embed = discord.Embed(
                        title=f'Comandos da Mitsuy [pág 1/3]',
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
                        \n[Instagram do dono](https://www.instagram.com/carlosdev10/)
                        \n[Servidor para suporte](https://discord.gg/9TcEt3bF)
                        """
                )
                embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                resposta = await message.send(embed=embed, delete_after=60)
                await resposta.add_reaction("1️⃣")
                await resposta.add_reaction("2️⃣")
                await resposta.add_reaction("3️⃣")
                break

            elif reaction.emoji == "2️⃣":
                embed = discord.Embed(
                        title=f'Comandos da Mitsuy [pág 2/3]',
                        colour= 0x0000ff,
                        description ="""Olá, muito obrigado por estar utilizando o bot Mitsuy.
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
                await resposta.add_reaction("1️⃣")
                await resposta.add_reaction("2️⃣")
                await resposta.add_reaction("3️⃣")
                break

            elif reaction.emoji == "3️⃣":
                embed = discord.Embed(
                        title=f'Comandos da Mitsuy [pág 2/3]',
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
                await resposta.add_reaction("1️⃣")
                await resposta.add_reaction("2️⃣")
                await resposta.add_reaction("3️⃣")
                break
            


def setup(bot):
    bot.add_cog(Help(bot))