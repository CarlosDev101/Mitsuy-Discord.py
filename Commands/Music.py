import discord
from discord.ext import commands
from discord.utils import get
from youtube_dl import YoutubeDL

class MusicYT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        self.is_playing = False
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        self.vc = ""
        
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False
        
        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            self.music_queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                self.vc = await self.music_queue[0][1].connect()
            else:
                await self.vc.move_to(self.music_queue[0][1])         
            print(self.music_queue)
            self.music_queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False
            await self.vc.disconnect()

    @commands.guild_only()
    @commands.command(name="Play", help="Toca uma música do YouTube",aliases=["play", 'p','tocar'])
    async def p(self, ctx, *args):
        query = " ".join(args)  
        try:
            voice_channel = ctx.author.voice.channel
        except:
            embed = discord.Embed(
                title="Aviso Importante",
                colour= 0x0000ff,
                description = 'Para tocar uma música, primeiro se conecte a um canal de voz.'
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.reply(embed=embed)
            return
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                embed = discord.Embed(
                    title="Algo deu errado",
                    colour= 0x0000ff,
                    description = 'Algo deu errado! Tente mudar a música ou mudar a playlist'
                )
                embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="Música adicionada",
                    colour= 0x0000ff,
                    description = f"Você adicionou a música **{song['title']}** à fila!"
                )
                embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed=embed)
                self.music_queue.append([song, voice_channel])
                
                if self.is_playing == False:
                    await self.play_music()

    @commands.guild_only()
    @commands.command(name="Pause", aliases=["pause", "pausa", "Pausa", "Stop", "stop"], help="Pausa a musica")
    async def pause(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            embed = discord.Embed(
                title="Música Pausada",
                colour= 0x0000ff,
                description = 'Sua música foi pausada.'
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Algo deu errado",
                colour= 0x0000ff,
                description = 'Não foi possivel pausar sua música.'
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed)           

    @commands.guild_only()
    @commands.command(name="Resume", aliases=["resume", "Despausar", "despausar"], help="Despausa a musica")
    async def reume(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_paused():
            embed = discord.Embed(
                title="Música Despausada",
                colour= 0x0000ff,
                description = 'Sua música foi despausada.'
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Algo deu errado",
                colour= 0x0000ff,
                description = 'Não foi possivel despausarpausar sua música.'
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed) 

    @commands.guild_only()
    @commands.command(name="Queue", help="Mostra as atuais músicas da fila.",aliases=["queue", 'q','fila'])
    async def q(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += f'**{i+1} - **' + self.music_queue[i][0]['title'] + "\n"

        print(retval)
        if retval != "":
            embed = discord.Embed(
                colour= 0x0000ff,
                description = f"{retval}"
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Algo deu errado",
                colour= 0x0000ff,
                description = 'Não existe músicas na fila no momento.'
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed)
    
    @commands.guild_only()
    @commands.command(name="skip", help="Pula a atual música que está tocando.",aliases=['pular'])
    @commands.has_permissions(manage_channels=True)
    async def skip(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            await self.play_music()
            embed = discord.Embed(
                title="Música pulada",
                colour= 0x0000ff,
                description = f"Você pulou a música."
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)            
            await ctx.send(embed=embed)
            
    @skip.error
    async def skip_error(self,ctx,error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Acesso negado",
                colour= 0x0000ff,
                description = f"Você precisa da permissão **Gerenciar canais** para pular músicas."
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)                 
            await ctx.send(embed=embed)     
        else:
            raise error
            
def setup(bot):
    bot.add_cog(MusicYT(bot))
