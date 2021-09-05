import discord
import requests
from random import randint
import json
from discord import Embed
from colors import colors
# Function to fetch a random quote

# Function to get a random joke


def get_joke(jokeType='general', number=1) -> discord.Embed:
    '''
        Return a joke Embed to the calling variable
        Parameters:
            jokeType: Type of joke to fetch
            number: Number of jokes to fetch
        Returns:
            A joke Embed
    '''
    base_url = "https://official-joke-api.appspot.com"
    response = None
    if(jokeType == 'general'):
        if number == 10:
            # https://official-joke-api.appspot.com/random_ten
            response = requests.get(base_url + "/random_ten")
        else:
            response = requests.get(f"{base_url}/random_joke")
    else:
        if number == 10:
            response = requests.get(base_url + "/jokes/programming/ten")
        else:
            response = requests.get(f"{base_url}/jokes/programming/random")
    jokes = json.loads(response.text)
    quote = ""
    for joke in jokes:
        new_quote = joke['setup'] + " \n> " + joke['punchline'] + "\n"
        quote += new_quote
    randomIndex = randint(
        0, len(colors) - 1)    # get a random color
    joke_embed = Embed(title="Here is something for you by us.",
                       url="https://gdsc.community.dev/indian-institute-of-information-technology-surat/",
                       description=f'**{quote}**', colour=colors[randomIndex])
    joke_embed.set_author(
        name='GDSC IIIT Surat Bot', icon_url='https://pbs.twimg.com/profile_images/1304114355517173769/F1e86tGu_400x400.jpg')
    joke_embed.set_thumbnail(
        url='https://pbs.twimg.com/profile_images/1304114355517173769/F1e86tGu_400x400.jpg')
    joke_embed.add_field(
        name='Contribute', value='[To add your thoughts/code, or to make bugfixes, visit GitHub](https://github.com/DSC-IIIT-Surat/GDSCBot/issues)')
    joke_embed.set_footer(
        text='Collaborate and Contribute', icon_url='https://pbs.twimg.com/profile_images/1304114355517173769/F1e86tGu_400x400.jpg')
    print(quote)
    # await message.reply(embed=about_msg)
    return joke_embed
