from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
import random
import discord

class Pat:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def pat(self, context, member: discord.Member=None):
        """Pat your senpai/waifu or even the enemy!"""
        author = context.message.author.mention
        text = ("someone who is really worth it!")
        
        if member != None:
            mention = member.mention
            text = mention

        pat = "**{0} pats {1}!**"

        choices = fileIO("data/pat/syxactions/pat.json","load")		
                
        image = random.choice(choices)
        
        embed = discord.Embed(description=pat.format(author, text), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Pat(bot)
    bot.add_cog(n)
