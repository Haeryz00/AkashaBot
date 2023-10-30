import discord
import os

# Create a Discord client instance
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('!hello')

    # content = message.content.lower()

    # if content.startswith('Hello'):
    #     hello_response = "Nice to meet you! Hehe, I've actually been watching you for a long time already. My name's Nahida."\
    #     "I might look like a child, but don't be fooled: I understand this world much better than any grown-up. So... can we trade knowledge?"\
    #     "I want to hear all about your travel stories. So, what would you like to know in return."

    #     await message.channel.send(hello_response)
    
    # elif content.startswith('Good morning'):
    #     morning = "Good morning. We should get going right away. There are too many things in this world that you'll miss if you don't get there on time."
    #     await message.channel.send(morning)

    # elif content.startswith('Good afternoon'):
    #     afternoon = "Ah, time for a break. I'd really like a Berry & Mint Burst... If you get one for me, I'll tell you a couple of stories about the sun. Okay?."
    #     await message.channel.send(afternoon)

    # elif content.startswith('Good evening'):
    #     evening = "The sun's setting. It's time to wave goodbye and let the creatures of the night take center stage."
    #     await message.channel.send(evening)

    # elif content.startswith('Good night'):
    #     night = "You should go to sleep now. Don't worry, I've made sure there's a sweet dream waiting for you."
    #     await message.channel.send(night)

client.run('MTE2ODE3Njc0ODM4NzYzNTI2MA.GW5yZI.SLcyYIJf3KI1d3yPlRagzt0vBX1Uo8XOdlHrZA')
