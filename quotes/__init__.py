
'''
    Module to handle quote requests
'''
import requests
import discord
import json
from random import randint
from colors import colors
from discord import Embed
# Function to fetch a random quote


def get_quote() ->discord.Embed:
    '''
        Returns a random quote from the quote API
    '''
    response = requests.get("https://www.zenquotes.io/api/random")
    json_data = json.loads(response.text)

    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    randomIndex = randint(
        0, len(colors) - 1)
    quote_embed=Embed(title="Here is something for you by us.",
          url="https://gdsc.community.dev/indian-institute-of-information-technology-surat/",
          description=f'**{quote}**', colour=colors[randomIndex])
    quote_embed.set_author(
        name='GDSC IIIT Surat Bot',
        icon_url='https://pbs.twimg.com/profile_images/1304114355517173769/F1e86tGu_400x400.jpg')
    quote_embed.set_thumbnail(
        url='https://pbs.twimg.com/profile_images/1304114355517173769/F1e86tGu_400x400.jpg')
    quote_embed.add_field(
        name='Contribute',
        value='[To add your thoughts/code, or to make bugfixes, visit GitHub](https://github.com/DSC-IIIT-Surat/GDSCBot/issues)')
    quote_embed.set_footer(
        text='Collaborate and Contribute',
        icon_url='https://pbs.twimg.com/profile_images/1304114355517173769/F1e86tGu_400x400.jpg')

    return quote_embed
