from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
import random
import discord

class Hug:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hug(self, context, member: discord.Member=None):
        """Hug your senpai/waifu!"""
        author = context.message.author.mention
        text = ("himself, creepy ugghhh!!!!!")
        
        if member != None:
            mention = member.mention
            text = mention

        hug = "**{0} hugs {1}!**"

        choices = fileIO("data/hug/syxactions/hug.json","load")		
                
        image = random.choice(choices)
        
        embed = discord.Embed(description=hug.format(author, text), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Hug(bot)
    bot.add_cog(n)
