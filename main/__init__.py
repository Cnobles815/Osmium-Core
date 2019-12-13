import os

import discord
from discord.ext import commands

token = "NjI3NTA5MzEwMDExNzM2MDY2.XfPMJA.3j0IZ1sASItKSnBE5EG5PcprvTk"

client = discord.Client()

# bot = commands.Bot(command_prefix = '!O')
#
# @bot.command(name ='alive')

@client.event
async def on_ready():
    general_chat = client.get_channel(545387429612224532)
    bot_control = client.get_channel(552272896056360960)


    print(f'{client.user.name} has connected to Discord!')

    await bot_control.send("Connected.")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Osmium Network Discord!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    standard_response = "This is a test response from the Osmium Python Bot. My designer didn't come up with anything interesting for me to say."

    if message.content == '!O alive':
        response = standard_response;
        await message.channel.send(response)

    if message.content.find("bread") != -1 or message.content.find("Bread") != -1 or message.content.find(":bread:") != -1:
        await message.channel.send('Indeed, the bread must be gotten {0.author.mention}'.format(message))

    if message.content.find("bREaD") != -1:
        await message.channel.sent('How dare you defame the bread with such lazy attention attention to proper casing, {0.author.mention}.'.format(message))


client.run(token)