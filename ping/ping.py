import discord
from discord.ext import commands
import datetime
import time
from random import choice, randint

class ping:
    """Ping, with time"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Pong."""
        t1 = time.perf_counter()
        await self.bot.send_typing(ctx.message.channel)
        t2 = time.perf_counter()
        thedata = ("Time: " + str(round((t2-t1)*1000)) + " ms")
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        data = discord.Embed(title=("Pong"), description=thedata, colour=discord.Colour(value=color))
        data.set_image(url="http://touch.prodigy.co.id/wp-content/uploads/2015/04/36.gif")
        
        await self.bot.say(embed=data)
     

def setup(bot):
    n = ping(bot)
    bot.add_cog(n)
