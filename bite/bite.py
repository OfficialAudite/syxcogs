from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
import random
import discord

class Bite:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def bite(self, context, member: discord.Member=None):
        """Bite your senpai/waifu or even yourself!"""
        author = context.message.author.mention
        text = ("himself, eeuwww nasty!!")
        
        if member != None:
            mention = member.mention
            text = mention

        bite = "**{0} bites {1}!**"

        choices = fileIO("data/bite/syxactions/bite.json","load")		
                
        image = random.choice(choices)
        
        embed = discord.Embed(description=bite.format(author, text), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Bite(bot)
    bot.add_cog(n)
