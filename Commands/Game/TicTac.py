import discord, random
from discord.ext import commands

class TicToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    player1 = ""
    player2 = ""
    turn = ""
    gameOver = True
    board = []
    winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
    ]

    @commands.guild_only()
    @commands.command(name="Tictac", aliases=["tictoe", "Velha", "velha"], help="Jogo da velha")
    async def game(self, ctx, p1: discord.Member, p2: discord.Member):
        global count
        global player1
        global player2
        global turn
        global gameOver

        if self.gameOver:
            global board
            board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
            turn = ""
            gameOver = False
            count = 0
            player1 = p1
            player2 = p2
            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + board[x]
            
                    num = random.randint(1, 2)
            if num == 1:
                turn = player1
                embed = discord.Embed(
                    title="<@" + str(player1.id) + "> começa com você",
                    description="Digite a coluna e a linha na qual você quer jogar.",
                    color=0x0000ff
                )
                embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed=embed)
            elif num == 2:
                embed = discord.Embed(
                    title="<@" + str(player1.id) + "> começa com você",
                    description="Digite a coluna e a linha na qual você quer jogar.",
                    color=0x0000ff
                )
                embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="Um jogo está em progresso",
                    description="Termine primeiro este jogo para começar outro.",
                    color=0x0000ff
                )
                embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed=embed)
    
    @commands.guild_only()
    @commands.command(name="Linha", aliases=["linha"], help="Posicao da jogada")
    async def linha(self, ctx, pos: int):
        global turn
        global player1
        global player2
        global board
        global count
        global gameOver

        if not gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"
                elif turn == player2:
                    mark = ":o2:"
                if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                    board[pos - 1] = mark
                    count += 1

                    # print the board
                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + board[x]
                    
                    def checkWinner(winningConditions, mark):
                        global gameOver
                        for condition in winningConditions:
                            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                                gameOver = True

                    checkWinner(self.winningConditions, mark)
                    if gameOver == True:
                        embed = discord.Embed(
                            title=f"{mark} você venceu",
                            description="Caramba que jogada foi essa... Parabens por ter vencido!",
                            color=0x0000ff
                            )
                        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                        await ctx.send(embed=embed)

                    elif count >= 9:
                        gameOver = True
                        embed = discord.Embed(
                            title="Empate",
                            description="Jogue novamente para desempatar.",
                            color=0x0000ff
                            )
                        embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                        await ctx.send(embed=embed)


                    # switch turns
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1
                else:
                    embed = discord.Embed(
                            title="Ei, preste atenção",
                            description="Certifique-se de escolher um número inteiro entre 1 e 9 (inclusive) e um bloco não marcado.",
                            color=0x0000ff
                        )
                    embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                    await ctx.send(embed=embed)                   
            else:
                embed = discord.Embed(
                    title="Ei, preste atenção",
                    description="Não é sua vez de jogar.",
                    color=0x0000ff
                )
                embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed=embed)  
        else:
                embed = discord.Embed(
                    title="Ei, preste atenção",
                    description="Por favor, inicie um jogo digitando o comando: !Tictac.",
                    color=0x0000ff
                )
                embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed=embed)
    
    @game.error
    async def game_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Ei, preste atenção",
                description=f"{ctx.author.mention} Por favor marque o @ de dois jogadores.",
                color=0x0000ff
                )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed)    
        
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title="Ei, preste atenção",
                description=f"{ctx.author.mention} Certifique-se de mencionar os jogadores (ie. <@688534433879556134>).",
                color=0x0000ff
            )
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed)   


    @linha.error
    async def linha_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Ei, preste atenção",
                description="Certifique-se de escolher um número inteiro entre 1 e 9 (inclusive) e um bloco não marcado.",
                color=0x0000ff
                )   
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed)  

        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title="Ei, preste atenção",
                description="Certifique-se de escolher um número inteiro entre 1 e 9 (inclusive) e um bloco não marcado.",
                color=0x0000ff
            )   
            embed.set_author(name= self.bot.user.name, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed=embed)  



def setup(bot):
    bot.add_cog(TicToe(bot))
