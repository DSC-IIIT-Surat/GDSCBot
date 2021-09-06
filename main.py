#!gdsc_bot_env/bin/python3
# Path: main.py
# *-* coding: utf-8 *-*
# Author: @AvanishCodes
# Email: avanishcodes@gmail.com
# Date: 2021-27-08
# Version: 0.1.0
# Description: A discord bot for Google Developer Students Club, Indian Institute of Information Technology, Surat for managing the Discord server.

'''
    GDSC Bot to be used for Google Developers Club, Indian Institute of Information Technology, Surat.
    @Contributors:
        - @AvanishCodes
        - @prakhar728
'''

# Libraries
import os
import json
import random
import discord
from colors import colors
from jokes import get_joke
from about import get_about
from quotes import get_quote
from dotenv import load_dotenv

# Environment Variable Settings
load_dotenv()
my_secret = os.getenv('TOKEN')
ANNOUNCEMENT_PASSWORD = os.getenv('ANNOUNCEMENT_PASSWORD')
ANNOUNCEMENT_CHANNEL = os.getenv('ANNOUNCEMENT_CHANNEL')
AUTHORIZED_MODS = f'post {ANNOUNCEMENT_PASSWORD}'
client = discord.Client()


@client.event
async def on_ready() -> None:
    '''
        Called when the bot is ready to start.
        Notifies the administrator that the bot is running.
    '''
    print('Bot has logged in as {0.user}'.format(client))


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
        await message.reply(embed=get_quote())

    # Random joke from the list
    elif message.content.startswith('$joke'):
        message_content = message.content.split(' ')
        # Number of jokes to be sent
        number_of_jokes = 1
        if len(message_content) > 1:
            number_of_jokes = 10
        # Category of joke to be sent
        jokeType = 'general'
        if len(message_content) > 2:
            jokeType = 'programming'
        await message.reply(embed=get_joke(jokeType=jokeType, number=number_of_jokes))

    # Starts with $about
    elif message.content.lower().startswith('$about'):
        await message.reply(embed=get_about())

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
            await message.reply(embed=get_about())

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

    # Format of a message in Discord server is: https://discord.com/channels/<server-id>/,channel-id>/<message-id>

'''
    Run the bot
'''


def main():
    '''
        Driver code for the bot.
    '''
    client.run(my_secret)


# Entry point for code
if __name__ == '__main__':
    main()
