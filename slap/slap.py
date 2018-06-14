from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
import random
import discord

class Slap:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def slap(self, context, member: discord.Member=None):
        """Slap your cursed enemy!"""
        author = context.message.author.mention
        text = ("someone secretly...")
        
        if member != None:
            mention = member.mention
            text = mention

        slap = "**{0} slaps {1}!**"

        choices = fileIO("data/slap/syxactions/slap.json","load")		
                
        image = random.choice(choices)
        
        embed = discord.Embed(description=slap.format(author, text), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Slap(bot)
    bot.add_cog(n)
