from asyncio.windows_events import NULL
import discord
import os
import random
import requests
import json
#from dotenv import load_dotenv

#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')

from discord.ext.commands import bot
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix = ".")


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)

@client.event
async def on_ready():
    print('Neural Link : Accessed : Welcome, {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

# Greeter
@client.event
async def on_member_join(member):
    channel = client.get_channel('🧤-ladder-rungs-🧤')
    embed=discord.Embed(title="Welcome!",description=f"{member.mention} connected using neural lace node #" + random(96))
    await channel.send(embed=embed)

if message.author == client.user:
    return

if message.channel.name == '🕋the-baud🕋' or message.channel.name == 'lab':

# Words to start milly to say inspirational quotes
if user_message.lower() == 'inspire me':
    await message.channel.send(f'See you later {username}!')
    return

# Words to catch
if user_message.lower() == 'hello' or 'hello milly' or 'milly':
	await message.channel.send(f'Hello {username}! \n\n Welcome to 🕋the-baud🕋 were we talk about taking over the world. 🌎 \n\n One mind at a time.. 🧠')
    return

if user_message.lower() == 'bye' or 'laters' or 'see ya':
	await message.channel.send(f'See you later {username}! 🖐\n\n 🕋the-baud🕋 Will miss you. 💨\n\n Come back soon!!] 💔\n\n 01110111 01100101 00100000 01101110 01100101 01100101 01100100 00100000 01111001 01101111 01110101 01110010 00100000 01100010 01110010 01100001 01101001 01101110')
	return

if user_message.lower() == 'what is the baud' or 'explain baud':
	await message.channel.send(f'Well {username}! \n\n *In telecommunication and electronics, baud is a common unit of measurement of symbol rate, which is one of the components that determine the speed of communication over a data channel.*')
	return

if user_message.lower() == 'baud':
	await message.channel.send(f'🕋the-baud🕋 sees {username}! \n\n Bit rate/Number of bits r = R/n\n')
	await message.channel.send(my_baud)
	return

if user_message.lower() == 'neural network':
	await message.channel.send(f'My Neural Network is at version 0.1')
	await message.channel.send(f'@dEEdEE is trying his best you should give him your support!')
	return
       
# Place all commands below here
if message.content.startswith('!commands'):
#	wait message.channel.send('*******************')
	await message.channel.send('!random')
	await message.channel.send('!inspire')
	await message.channel.send('!98■97■117■100-simpCrypt')
	await message.channel.send('!119■101■108■111■118■101■109■105■108■108■121■116■111■46■98■97■116-simpCrypt')
	return

if message.content.startswith('!random'):
	response = f'This is your random number: {random.randrange(1000000)}'
	await message.channel.send(response)
	return

if message.content.startswith('!inspire'):
	quote = get_quote()
	await message.channel.send(quote)
	return(quote)

if message.content.startswith('!baud'):
	await message.channel.send('This is our world now... the world of the electron and the switch, the beauty of the baud.')
	return

if message.content.startswith('!welovemillyto.bat'):
	await message.channel.send('*******************')
	await message.channel.send('1:) !link')
	await message.channel.send('2:) !secret')
	return

if message.content.startswith('!link'):
	await message.channel.send('https://floats.city/0x913a33a6cb3211db/event/253039470')
	return

if message.content.startswith('!secret'):
	await message.channel.send(' 00100011 01101001 01000010 01100101 01101100 01101001 01100101 01110110 01100101 00101110 01100010 01100001 01110100')
	return

with open("TOKEN.0", "r", encoding="UTF-8") as f:
    bottoken = f.read()
    
client.run(bottoken)