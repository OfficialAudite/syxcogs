from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
import random
import discord

class Punch:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def punch(self, context, member: discord.Member=None):
        """Punch your enemy or even yourself!"""
        author = context.message.author.mention
        text = ("at someone...")
        
        if member != None:
            mention = member.mention
            text = mention

        punch = "**{0} punches {1}!**"

        choices = fileIO("data/punch/syxactions/punch.json","load")		
                
        image = random.choice(choices)
        
        embed = discord.Embed(description=punch.format(author, text), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Punch(bot)
    bot.add_cog(n)
