import discord
import random
import datetime
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

        author = ctx.message.author                         #Here we get the Author Object
        author_id = float(author.id)                              #Here we Get his ID
        author_name, author_code = str(author).split("#")   #We split his name as a string

        #Removed the if and the base atrget because you need a user to ship with!!
        user_id = float(user.id)                                   #Here get the user ID
        user_name, user_code = str(user).split("#")         #Cast user to a str and split at the same time
        target = user_name                                  #Set the target Name

        now = datetime.datetime.now()                       #Create datetime Object
        day_seed = (now.day + now.month + now.year) / 3     #Generate the date seed by doing the average of the current day month and year
        seed = (author_id + user_id) / day_seed         #Generate the Ship seed by dadding both author and user IDs and dividing it by time seed
        random.seed(seed)                                   #Apply the seed to the generator
        rate =  random.randint(1, 99)                       #Generate the Ship %

        mess = "Love rate between " + author_name + " and " + target + " is " + str(rate) + "%"

        try:
                b = discord.Embed(color = discord.Color(0xeb1818), title = (str(mess)))
                await self.bot.say(embed=b)

        except errors.BadArgument:
                await self.bot.say("Oops, something went wrong! try again later!")

def setup(bot):
    bot.add_cog(Ship(bot))
