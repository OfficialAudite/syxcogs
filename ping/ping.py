import discord
from discord.ext import commands
from .utils.dataIO import fileIO
import datetime
import time
from random import choice, randint, random

class ping:
    """Ping, with time"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Pong."""
        choices = fileIO("data/ping/syxactions/ping.json","load")
        image = random.choice(choices)
        t1 = time.perf_counter()
        await self.bot.send_typing(ctx.message.channel)
        t2 = time.perf_counter()
        thedata = ("Time: " + str(round((t2-t1)*1000)) + " ms")
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        data = discord.Embed(title=("Pong"), description=thedata, colour=discord.Colour(value=color))
        data.set_image(url="image")
        
        await self.bot.say(embed=data)
     

def setup(bot):
    n = ping(bot)
    bot.add_cog(n)
