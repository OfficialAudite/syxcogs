import discord
from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
from random import choice as rnd

class Mad:

    def __init__(self, bot):
        self.bot = bot
        self.mad_images = fileIO("data/mad/syxactions/mad.json","load")

    @commands.command(pass_context=True)
    async def mad(self, ctx, user: discord.Member=None):
        """It's a action if you are mad. Tag a person too!"""

        author = str(ctx.message.author)
        author_name, author_code = author.split("#")
        target = "you!!!!!"
		
        if user != None:
            user = str(user)
            user_name, user_code = user.split("#")
            target = user_name
        try:

                b = discord.Embed(color = discord.Color(0xA4DAC4), title = (author_name + " is very mad at " + target))
                b.set_image(url=rnd(self.mad_images))
                await self.bot.say(embed=b)

        except errors.BadArgument:
                await self.bot.say("Oops, a mad picture couldn't be sent! Try again later")

def setup(bot):
    bot.add_cog(Mad(bot))