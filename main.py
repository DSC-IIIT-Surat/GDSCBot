#!gdsc_bot_env/bin/python3
# Path: main.py
# *-* coding: utf-8 *-*
# Author: @AvanishCodes
# Email: avanishcodes@gmail.com
# Deployment Managed by prakash-cr7
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
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from colors import colors
from jokes import get_joke
from about import get_about
from quotes import get_quote
from dotenv import load_dotenv

# Environment Variable Settings
load_dotenv()
my_secret = os.getenv('TOKEN')
ANNOUNCEMENT_PASSWORD = os.getenv('ANNOUNCEMENT_PASSWORD')
ANNOUNCEMENT_CHANNEL = int(os.getenv('ANNOUNCEMENT_CHANNEL'))
DEVHEAT_ANNOUNCE_CHANNEL = int(os.getenv('DEVHEAT_ANNOUNCEMENT_CHANNEL'))
AUTHORIZED_MODS = f'post {ANNOUNCEMENT_PASSWORD}'
DEVHEAT_AUTHORIZED_MODS = f'post {os.getenv("DEVHEAT_ANNOUNCEMENT_PASSWORD")}'

client = discord.Client()
client = commands.Bot(command_prefix='$')  # put your own prefix here


@client.event
async def on_ready() -> None:
    '''
        Called when the bot is ready to start.
        Notifies the administrator that the bot is running.
    '''
    print('Bot has logged in as {0.user}'.format(client))



@client.command(name='ping')
async def ping(message):
    # simple command so that when you type "!ping" the bot will respond with "pong!"
    await message.reply("Pong! I am online, use **$help** for help.")

@client.command(name='about')
async def ping(message):
    # simple command so that when you type "!ping" the bot will respond with "pong!"
    await message.reply(embed=get_about())

@client.command(name='hello')
async def ping(message):
    # simple command so that when you type "!ping" the bot will respond with "pong!"
    await message.reply(f'Hi {message.author.mention}!\n> Use **$help** to see a list of commands')

@client.command(pass_context=True, name='role')
async def give_theme_role(message, role_name):
    '''Assign a new role to the user

    Parameters
    ----------
    message : discord.Message
        The message object that triggered the command.
    role_name : str
        The name of the role to assign to the user.

    Returns
    -------
    None
    '''

    print("Hi ", role_name)
    # DevHeat Server Number: 778169072013017099
    target_server_id = 778169072013017099
    target_role_id = int()
    roles = {
        'education': 905450394400989184,
        'health': 905450492417683457,
        'infra': 905450543139409930,
        'social': 905450576240844880,
        'agriculture': 905450642045292584,
        'fintech': 905450619945508926
    }
    member = message.message.author
    target_role = get(member.guild.roles, id=roles[role_name])
    await member.add_roles(target_role)
    await message.channel.send(f'{member.mention} has been given the role {target_role.name}')

    '''
    if role_name in roles:
        target_role_id = roles[role_name]
    else:
        message.channel.send(f'{role_name} is not a valid role.')
        return
    # Assign the role
    member = message.author
    await member.add_roles(discord.Role(target_role_id))
    # Check if the user is already in the role
    if target_role_id in [role.id for role in member.roles]:
        await message.channel.send(f'{member.mention} already has the role {role_name}.')
        return
    
    # Check if the user is in the server
    if member.guild.id != target_server_id:
        await message.channel.send(f'{member.mention} is not in the server.')
        return
    
    # Check if the role exists
    role = get(member.guild.roles, id=target_role_id)
    if role is None:
        await message.channel.send(f'The role {role_name} does not exist.')
        return
    
    # Assign the role
    role = discord.utils.get(message.guild.roles, id=target_role_id)
    await member.add_role(role)

    # if not message.message.channel.is_private:
    #     await client.say("Private command only")
    server = await client.get_server(target_server_id)
    role = discord.utils.get(server.roles, id=target_role_id)
    member = server.get_member(message.message.author.id)
    if member:
        await member.add_roles(member, role)
    else:
        await client.say("You are not a member")
    '''

'''
@client.command(name='help')
async def help(message):
    helpType = message.content.split(' ')[-1]
    if helpType == None:
        await message.reply(f'List of commands:\n> $quote : get a random quote. \n> $motivate : get a random quote\n> $hello : A test command for interaction\n> $ping : status message to check if the bot is working\n> $ticket : appoint a mod to help someone based on the tech stack\n> $post : post a new announcement in announcement channel')
    elif helpType == 'ticket':
        await message.reply(f'To appoint a mod, use $ticket <tech stack>')
    elif helpType == 'ping':
        await message.reply(f'To check if the bot is working, use $ping')
    elif helpType == 'about':
        await message.reply(embed=get_about())
'''

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
    # elif message.content.lower().startswith('$ping'):
    #     await message.reply('Pong! I am alive.')

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
    await client.process_commands(message)

    # Designed Separately for DevHeat
    if message.content.startswith(f"{DEVHEAT_AUTHORIZED_MODS}"):
        # channel ID of announcement channel
        channel = client.get_channel(DEVHEAT_ANNOUNCE_CHANNEL)
        randomIndex = random.randint(
            0, len(colors) - 1)    # get a random color
        l_msg = discord.Embed(  # create embed object
            title=str(''.join(message.content.split('\n')[1])),
            description=str('\n'.join(message.content.split('\n')[2:])),
            colour=colors[randomIndex])
        await channel.send(embed=l_msg)
    # await client.process_commands(message)

    # Format of a message in Discord server is: https://discord.com/channels/<server-id>/,channel-id>/<message-id>


'''
async def kick(ctx, member: discord.Member):
    try:
        await member.kick(reason=None)
        # simple kick command to demonstrate how to get and use member mentions
        await ctx.send("kicked "+member.mention)
    except:
        await ctx.send("bot does not have the kick members permission!")
'''


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