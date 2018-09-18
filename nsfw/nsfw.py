from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
import random
import discord

class Nsfw:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def nsfw(ctx, self, context, member: discord.Member=None):

pictures = fileIO("data/punch/syxactions/nsfw.json","load")

if ctx.channel.is_nsfw():
    ctx.send("U can't use that command in a non NSFW channel!")
else:
    text = ("Testing new NSFW features.")
    image = random.choice(pictures)
    embed = discord.Embed(description=nsfw.format(text), colour=discord.Colour.red())
    embed.set_image(url=image)

    await self.bot.say(embed=embed)

def setup(bot):
    n = Nsfw(bot)
    bot.add_cog(n)
