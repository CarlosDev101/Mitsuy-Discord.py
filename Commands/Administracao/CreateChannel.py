import discord
from discord.ext import commands

class CreateChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #CRIAR CANAL

    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    @commands.command(name="Createchannel", aliases=['criarcanal', "createchannel"], help="Cria um canal de texto")
    async def createchannel(self, ctx, *, channelName):
        embed = discord.Embed(
            title = "Acesso liberado",
            description = "O chat {channelName} foi criado!",
            color = 0x0000ff
        )
        embed.add_field(value=f'**Canal criado por:** {ctx.author.mention} ')
        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
        await ctx.guild.create_text_channel(name=f'{channelName}')
        await ctx.send(embed=embed)
        await ctx.message.delete()
    
    @createchannel.error
    async def criarcanal_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
            title='Acesso negado',
            description='Ops, parece que você não tem permissão para usar este comando!',
            color= 0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()
        
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='Parece que você esqueceu de algo...',
                description='Escreva o nome do canal de texto que você quer criar.',
                color= 0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed, delete_after=60)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(CreateChannel(bot))