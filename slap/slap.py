import discord
from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
from random import choice as rnd

class Slap:

    def __init__(self, bot):
        self.bot = bot
        self.slap_images = fileIO("data/slap/syxactions/slap.json","load")

    @commands.command(pass_context=True)
    async def slap(self, ctx, user: discord.Member=None):
        """It's a action if you want to slap someone. Tag a person too!"""

        #author = ctx.message.author
        
        author = str(ctx.message.author)
        author_name, author_code = author.split("#")
		
        target = "someone while hidden.."
        if user != None:
            user = str(user)
            user_name, user_code = user.split("#")
            target = user_name

        try:
                b = discord.Embed(color = discord.Color(0xA4DAC4), title = (author_name + " slaps " + target))
                b.set_image(url=rnd(self.slap_images))
                await self.bot.say(embed=b)

        except errors.BadArgument:
                await self.bot.say("Oops, a slap picture couldn't be sent! Try again later")

def setup(bot):
    bot.add_cog(Slap(bot))