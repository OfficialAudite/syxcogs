import discord
import random
from discord.ext import commands
from discord.ext.commands import errors, converter
from .utils.dataIO import fileIO
from random import choice as rnd

class Ship:
    def __init__(self, bot):
        self.bot = bot
    def __getitem__(self,x):
    	self.x = x
     

    @commands.command(pass_context=True)
    async def ship(self, ctx, user: discord.Member):
        """not sure but it's probably random. Tag a person!"""

        #author = ctx.message.author
        
        author = str(ctx.message.author)
        author_name, author_code = author.split("#")
		
        target = "himself, creepy ugghhh!!!!!"
        if user != None:
            user = str(user)
            user_name, user_code = user.split("#")
            target = user_name

        
    
        rate =  random.randint(1, 99)


        mess = "love rate between " + author_name + " and " + target + " is " + str(rate) + "%"



        try:
                b = discord.Embed(color = discord.Color(0xeb1818), title = (str(mess)))
                await self.bot.say(embed=b)

        except errors.BadArgument:
                await self.bot.say("Oops, something went wrong! try again later!")

def setup(bot):
    bot.add_cog(Ship(bot))