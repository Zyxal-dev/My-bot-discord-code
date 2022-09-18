try:
	import discord, colorama, requests, math, random, asyncio
	from discord.ext import commands
	from discord.ext.commands.core import command
	from discord import utils
	from colorama import Fore
	import config
	from test import number
except ImportError:
    input ("If you not install the requirements.txt -- Will not work! [ *Press enter to start* ]:")

channelIDS = 1015684903435776082

client = commands.Bot(command_prefix = '.', intents = discord.Intents.all(), case_insensitive=True)
client.remove_command("help")
# .hello
client = commands.Bot(command_prefix = '.', intents = discord.Intents.all(), case_insensitive=True)
client.remove_command("help")

# def progress_bar1 #
#def progress_bar1( progress,total,color=colorama.Fore.YELLOW ):
    #percent = 100 * (progress / float (total))
    #bar = '█' * int (percent) + '-' * (100 - int (percent))
    #print (color + f"\r|{bar}| {percent:.2f}%",end="\r")
    #if progress == total:
        #print (colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%",end="\r")

#numbers1 = [x * 5 for x in range (3000,3500)]
#results1 = []

# progress_bar1 #
#progress_bar1 (0,len (numbers1))
#for i,x in enumerate (numbers1):
    #results1.append (math.factorial (x))
    #progress_bar1 (i + 1,len (numbers1))

#print (colorama.Fore.RESET)

#print(' ')

@client.event

async def on_ready():
	print(' ')
	print(' ')
	print('[MODER] - ⚡Zyxal⚡ = Bot - Successfully Logged in system DISCORD SERVER!')

@client.event
async def on_member_join(member):
	print(f"{member} has joined!")
	await client.get_channel(1015684903435776082).send("Добро пожаловать в "+"***{}***, Прочитайте правила сервера в канале ruls".format(member.guild.name)+" "+"{}".format(member.mention))

@client.event
async def on_member_remove(member):
	print(f"{member} leave the server!")
	await client.get_channel(1015684903435776082).send("Вышёл из сервера "+"***{}***".format(member.guild.name)+" "+"{}".format(member.mention))


#@client.event
#async def on_member_join(member):
  	#print(f"{member} has joined!")

@client.command(pass_context = True)

async def hello(ctx):
	await ctx.send('Welcome, to the Zyxal - TEAM')

@client.command(pass_context = True)

async def link(ctx):
	await ctx.send('https://github.com/Zyxal-dev')

@client.command(pass_context = True)
async def clear(ctx, amount=10):
	await ctx.channel.purge(limit=amount)
	await ctx.send(f'Удалено {amount} сообщений!', delete_after = 3)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'Kicked {member.mention}', delete_after = 3)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'Banned {member.mention}', delete_after = 3)

# Connect
token = open('token.txt', 'r').readline()

client.run(token)

#intents = discord.Intents.default()
#intents.message_content = True
#, intents=intents

#@client.command(pass_context = True)

#async def hello(ctx):
	#await ctx.send('Welcome, to the Zyxal - GROUP')

#@client.command(pass_context = True)

#async def link(ctx):
	#await ctx.send('https://github.com/Zyxal-dev')