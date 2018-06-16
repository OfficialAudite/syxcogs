from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
import random
import discord

class Kiss:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def kiss(self, context, member: discord.Member=None):
        """Kiss your senpai/waifu or even the enemy!"""
        author = context.message.author.mention
        text = ("a secret ghost!!")
        
        if member != None:
            mention = member.mention
            text = mention

        kiss = "**{0} kisses {1}!!**"

        choices = fileIO("data/kiss/syxactions/kiss.json","load")		
                
        image = random.choice(choices)
        
        embed = discord.Embed(description=kiss.format(author, text), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Kiss(bot)
    bot.add_cog(n)