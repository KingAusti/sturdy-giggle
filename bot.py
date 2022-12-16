import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

    @client.event
    async def on_message(message):
        if 'rick' in message.content.lower():
            await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

client.run('MTA1MzQ1Nzg0OTM1NjkyNzAyNg.GLWl9L.bl_OlYf2pANYvmBD3rqAWm2EQhBPfLDbRk-_-w')