#!gdsc_bot_env/bin/python3
# Path: main.py
# *-* coding: utf-8 *-*
# Author: @AvanishCodes
# Date: 2021-27-08
# Version: 0.1.0
# Description: A discord bot for Google Developer Students Club, Indian Institute of Information Technology, Surat for managing the Discord server.

# Libraries
import os
import json
import random
import discord
from quotes import get_quote
from dotenv import load_dotenv

# Environment Variable Settings
load_dotenv()
my_secret = os.getenv('TOKEN')
AMMOUNCEMENT_PASSWORD = os.getenv('AMMOUNCEMENT_PASSWORD')
ANNOUNCEMENT_CHANNEL = os.getenv('ANNOUNCEMENT_CHANNEL')
client = discord.Client()

# For letting the administrator know that the bot is running


@client.event
async def on_ready():
    print('Bot has logged in as {0.user}'.format(client))


# Colors array for randomly selecting a color for embeds
colors = [
    discord.Color.teal(),
    discord.Color.dark_teal(),
    discord.Color.green(),
    discord.Color.dark_green(),
    discord.Color.blue(),
    discord.Color.dark_blue(),
    discord.Color.purple(),
    discord.Color.dark_purple(),
    discord.Color.magenta(),
    discord.Color.dark_magenta(),
    discord.Color.gold(),
    discord.Color.dark_gold(),
    discord.Color.orange(),
    discord.Color.dark_orange(),
    discord.Color.red(),
    discord.Color.dark_red(),
    discord.Color.lighter_grey(),
    discord.Color.dark_grey(),
    discord.Color.light_grey(),
    discord.Color.darker_grey(),
    discord.Color.blurple(),
    discord.Color.greyple(),
]


# Reply to the messages
@client.event
async def on_message(message):
    '''
        This function is called when a message is sent in the discord server.
        Messages can start with:
            $quote      : send a random quote from zenquotes.io
            $motivate   : send a random quote zenquotes.io
            $hello      : A test command for interaction
            $help       : send a list of commands
            $ping       : send a status message to check if the bot is working
            $ticket     : appoint a mod to help someone based on the tech stack
            $post       : post a new announcement in announcement channel
            $about      : send a  desciption of club and bot
    '''
    if message.content.startswith('$quote'):            # $quote
        await client.send_message(message.channel, get_quote())

    # Random quote from the list
    elif message.content.startswith('$motivate'):
        await message.reply(get_quote())

    # Starts with $about
    elif message.content.lower().startswith('$about'):
        randomIndex = random.randint(
            0, len(colors) - 1)    # get a random color
        about_msg = discord.Embed(title="This bot is for managing the Discord server of Google Developer Students Club, Indian Institute of Information technoology, Surat.",
                                  url="https://gdsc.community.dev/indian-institute-of-information-technology-surat/", description="To know more about us, visit: https://gdsc.community.dev/indian-institute-of-information-technology-surat/'", colour=colors[randomIndex])
        about_msg.set_author(
            name='GDSC IIIT Surat Bot', icon_url='https://pbs.twimg.com/profile_images/1304114355517173769/F1e86tGu_400x400.jpg')
        about_msg.set_thumbnail(
            url='https://pbs.twimg.com/profile_images/1304114355517173769/F1e86tGu_400x400.jpg')
        about_msg.add_field(
            name='Contribute', value='[To add your thoughts/code, or to make bugfixes, visit GitHub](https://twitter.com/dsc_iiitsurat)')
        about_msg.set_footer(
            text='Collaborate and Contribute', icon_url='https://twitter.com/dsc_iiitsurat')
        await message.reply(embed=about_msg)

    # Test command
    elif message.content.lower().startswith('$hello'):
        await message.reply(f'Hi {message.author.mention}!\n> Use $help to see a list of commands')

    # help command
    elif message.content.lower().startswith('$help'):
        helpType = message.content.split(' ')[-1]
        if helpType == None:
            await message.reply(f'List of commands:\n> $quote : get a random quote. \n> $motivate : get a random quote\n> $hello : A test command for interaction\n> $ping : status message to check if the bot is working\n> $ticket : appoint a mod to help someone based on the tech stack\n> $post : post a new announcement in announcement channel')
        elif helpType == 'ticket':
            await message.reply(f'To appoint a mod, use $ticket <tech stack>')
        elif helpType == 'ping':
            await message.reply(f'To check if the bot is working, use $ping')
        elif helpType == 'about':
            randomIndex = random.randint(
                0, len(colors) - 1)    # get a random color
            about_msg = discord.Embed(title="This bot is for managing the Discord server of Google Developer Students Club, Indian Institute of Information technoology, Surat.",
                                      url="https://gdsc.community.dev/indian-institute-of-information-technology-surat/", description="To know more about us, visit: https://gdsc.community.dev/indian-institute-of-information-technology-surat/'", colour=colors[randomIndex])
            about_msg.set_author(
                name='GDSC IIIT Surat Bot', icon_url='https://pbs.twimg.com/profile_images/1304114355517173769/F1e86tGu_400x400.jpg')
            about_msg.set_thumbnail(
                url='https://pbs.twimg.com/profile_images/1304114355517173769/F1e86tGu_400x400.jpg')
            about_msg.add_field(
                name='Contribute', value='[To add your thoughts/code, or to make bugfixes, visit GitHub](https://twitter.com/dsc_iiitsurat)')
            about_msg.set_footer(
                text='Collaborate and Contribute', icon_url='https://twitter.com/dsc_iiitsurat')
            await message.reply(embed=about_msg)

    # Bot status test
    elif message.content.lower().startswith('$ping'):
        await message.reply('Pong! I am alive.')

    # Create a new support  ticket
    elif message.content.lower().startswith('$ticket'):
        techStack = message.content.split()[-1]
        if (techStack == 'python'):    # Web
            await message.reply(
                f"Wait {message.author.mention} <@737245346643837002> will reply your query."
            )
        elif (techStack == 'web' or techStack == 'js'):  # Mobile
            await message.reply(
                f"Wait {message.author.mention} <@737196876465438770> will reply your query."
            )

    # Post a new announcement
    AUTHORIZED_MODS = 'post {ANNOUNCEMENT_PASSWORD}'
    if message.content.startswith(AUTHORIZED_MODS):
        # channel ID of announcement channel
        channel = client.get_channel(ANNOUNCEMENT_CHANNEL)
        randomIndex = random.randint(
            0, len(colors) - 1)    # get a random color
        l_msg = discord.Embed(  # create embed object
            title=str(''.join(message.content.split('\n')[1])),
            description=str('\n'.join(message.content.split('\n')[2:])),
            colour=colors[randomIndex])
        await channel.send(embed=l_msg)

    return


# Driver Code
def main():
    client.run(my_secret)


# Entry point for code
if __name__ == '__main__':
    main()
