from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
import random
import discord

class Execute:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def execute(self, context, member: discord.Member=None):
        """Execute your senpai/waifu or even yourself!"""
        author = context.message.author.mention
        text = ("himself...")
        
        if member != None:
            mention = member.mention
            text = mention

        execute = "**{0} executes {1}!**"

        choices = fileIO("data/execute/syxactions/execute.json","load")		
                
        image = random.choice(choices)
        
        embed = discord.Embed(description=execute.format(author, text), colour=discord.Colour.red())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Execute(bot)
    bot.add_cog(n)
