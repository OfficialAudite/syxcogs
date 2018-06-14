from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
import random
import discord

class Pout:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def pout(self, context, member: discord.Member=None):
        """Pout at your senpai/waifu or even yourself!"""
        author = context.message.author.mention
        text = ("someone...")
        
        if member != None:
            mention = member.mention
            text = mention

        pout = "**{0} pouts at {1}!**"

        choices = fileIO("data/pout/syxactions/pout.json","load")		
                
        image = random.choice(choices)
        
        embed = discord.Embed(description=pout.format(author, text), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Pout(bot)
    bot.add_cog(n)
