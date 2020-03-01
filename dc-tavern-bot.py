# bot.py
import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user or str(message.channel) != 'bot-testing':
        return

    introduction_quotes = [
        'Sivaslı Taverne hoş geldin, sol tarafta Kimya masasını ve köşede takılan mültecileri bulabilirsin. Koridorun sonunda ise akşamları canlı müzik var kalıbalıktan fark edersin zaten.',
        'havhav.... ba dum tsss',
        'Bira sadece 3 gold!! kaçırma derim!',
        'Maelestorm\'un bana 34 gold borcu var, onu bulursam Draugrlara yem edeceğim!!']

    if 'bilgi' or 'tavern' in message.content.lower():
        response = random.choice(introduction_quotes)
        await message.channel.send(response)
    elif 'fotograf' or 'görüntü' or 'nerede' or 'nerde' or 'benziyor':
        image = 'https://cdna.artstation.com/p/assets/images/images/002/810/298/large/guray-emen-2.jpg?1465984726'
        await message.channel.send(image)

client.run(TOKEN)
