import discord
from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
from random import choice as rnd

class Hug:

    def __init__(self, bot):
        self.bot = bot
        self.hug_images = fileIO("data/hug/syxactions/hug.json","load")

    @commands.command(pass_context=True)
    async def hug(self, ctx, user: discord.Member=None):
        """It's a action if you want to hug. Tag a person too!"""

        #author = ctx.message.author
        
        author = str(ctx.message.author)
        author_name, author_code = author.split("#")
		
        target = "himself, creepy ugghhh!!!!!"
        if user != None:
            user = str(user)
            user_name, user_code = user.split("#")
            target = user_name

        try:
                b = discord.Embed(color = discord.Color(0xA4DAC4), title = (author_name + " hugs " + target))
                b.set_image(url=rnd(self.hug_images))
                await self.bot.say(embed=b)

        except errors.BadArgument:
                await self.bot.say("Oops, a hug picture couldn't be sent! Try again later")

def setup(bot):
    bot.add_cog(Hug(bot))