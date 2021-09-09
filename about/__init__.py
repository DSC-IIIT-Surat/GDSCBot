import discord
from random import randint
from colors import colors
from dotenv import load_dotenv
from os import getenv
# Environment Variable Settings
load_dotenv()
PROFILE_PIC = getenv('PROFILE_PIC')

# Function to return an about embed


def get_about() -> discord.Embed:
    '''
    Returns an about embed
    '''
    randomIndex = randint(
        0, len(colors) - 1)    # get a random color
    about_msg = discord.Embed(title="This bot is for managing the Discord server of Google Developer Students Club, Indian Institute of Information technoology, Surat.",
                              url="https://gdsc.community.dev/indian-institute-of-information-technology-surat/",
                              description="To know more about us, visit: https://gdsc.community.dev/indian-institute-of-information-technology-surat/'",
                              colour=colors[randomIndex])
    about_msg.set_author(
        name='GDSC IIIT Surat Bot', icon_url=PROFILE_PIC)
    about_msg.set_thumbnail(
        url=PROFILE_PIC)
    about_msg.add_field(
        name='Contribute', value='[To add your thoughts/code, or to make bugfixes, visit GitHub](https://github.com/DSC-IIIT-Surat/GDSCBot/issues)')
    about_msg.set_footer(
        text='Collaborate and Contribute', icon_url=PROFILE_PIC)
    return about_msg
