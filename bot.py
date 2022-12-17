import discord
from bot_key import bot_credentials

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

    @client.event
    async def on_message(message):
        if 'rick' in message.content.lower():
            await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

client.run(bot_credentials)