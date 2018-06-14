from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
import random
import discord

class Mad:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def mad(self, context, member: discord.Member=None):
        """Be mad at your senpai/waifu or even yourself!"""
        author = context.message.author.mention
        text = ("someone...")
        
        if member != None:
            mention = member.mention
            text = mention

        mad = "**{0} is mad at {1}!**"

        choices = fileIO("data/mad/syxactions/mad.json","load")		
                
        image = random.choice(choices)
        
        embed = discord.Embed(description=mad.format(author, text), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Mad(bot)
    bot.add_cog(n)
