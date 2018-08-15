from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
import random
import discord

class Cuddle:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def cuddle(self, context, member: discord.Member=None):
        """Cuddle with your senpai/waifu or even yourself!"""
        author = context.message.author.mention
        text = ("himself...")
        
        if member != None:
            mention = member.mention
            text = mention

        cuddle = "**{0} cuddles with {1}!**"

        choices = fileIO("data/cuddle/syxactions/cuddle.json","load")		
                
        image = random.choice(choices)
        
        embed = discord.Embed(description=cuddle.format(author, text), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Cuddle(bot)
    bot.add_cog(n)
