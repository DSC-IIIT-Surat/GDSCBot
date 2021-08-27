import discord
from colors import colors


# Function to return an about embed
def get_about():
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
    return about_msg
