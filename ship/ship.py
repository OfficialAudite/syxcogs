import io
import random
import discord
import datetime
import requests
from discord.ext import commands
from discord.ext.commands import errors, converter
from PIL import Image, ImageFont, ImageDraw

class Ship:
    def __init__(self, bot):
        self.bot = bot
    def __getitem__(self,x):
        self.x = x


    @commands.command(pass_context=True)
    async def ship(self, ctx, user: discord.Member):
        """not sure but it's probably random. Tag a person!"""

        author = ctx.message.author                                         #Here we get the Author Object
        author_id = float(author.id)                                        #Here we Get his ID
        user_id = float(user.id)                                            #Here get the user ID

        now = datetime.datetime.now()                                       #Create datetime Object
        day_seed = (now.day + now.month + now.year) / 3                     #Generate the date seed by doing the average of the current day month and year
        seed = (author_id + user_id) / day_seed                             #Generate the Ship seed by dadding both author and user IDs and dividing it by time seed
        random.seed(seed)                                                   #Apply the seed to the generator
        rate =  random.randint(1, 99)                                       #Generate the Ship %

        user_avatar = get_avatar(user)                                      #Get user avatar from discord
        author_avatar = get_avatar(author)                                  #Get author avatar from discord

        if ((user_avatar and author_avatar != None)):                       #Test if got the avatars proprely
            self.make_image(author_avatar, user_avatar, author.name, user.name, rate) #Make the ship image from the avatars
            await self.img_ship(ctx, author.mention, user.mention, rate)    #Call image based ship command
        else:
            await self.text_ship(user.mention, author.mention, rate)        #Call text based ship command

    async def img_ship(self, ctx, author, user, rate):
        msg = "**The Love rate between {0} and {1} is {2}%!**"
        #### Discord.py version 1.0.0 or higher, embed image upload ####
        if discord.__version__ >= "1.0.0":
            try:
                b = discord.Embed(color = discord.Color(0xeb1818), description = msg.format(author, user, rate))
                f = discord.File("data/ship/tmp_ship.png")                  #Load image from local
                b.set_image(url="attachment://tmp_ship.png")                #Attach Image to embed
                await ctx.send(files=[f], embed=b)                          #Send image with embed

            except errors.BadArgument:
                await self.bot.say("Oop, something went wrong! try again later!")
        #### Discord.py inferior to 1.0.0 not embe supported ####
        else:
            try:
                await self.bot.send_file(ctx.message.channel, "data/ship/tmp_ship.png", content = msg.format(author, user, rate))

            except errors.BadArgument:
                await self.bot.say("Oops, something went wrong! try again later!")
    def make_image(self, author_avatar, user_avatar, author, user, rate):
        #Define colors
        red = (191, 15, 0, 255)                                             #Tuple that matche the red color
        white = (255, 255, 255, 255)                                        #Tuple that matche the white color
        blank = (255, 255, 255, 0)                                          #Tuple that matche the blank color

        #Open template
        tmpl = Image.open("data/ship/Template.png", "r").convert('RGBA')    #Open template Image
        fill = Image.open("data/ship/Tmpl_fill.png", "r").convert('RGBA')   #Open fill template
        blank = Image.new('RGBA', tmpl.size, blank)                         #Blank image to write the text and paste fill
        fnt = ImageFont.truetype("data/ship/font.ttf", 17)                  #Load font
        draw = ImageDraw.Draw(blank)                                         #Create drawing context

        tmpl.paste(author_avatar, (0, -5))                                  #Paste Author avatar on the template
        tmpl.paste(user_avatar, (0, 133))                                   #Paste User avatar on the template
        offset = 100 - rate                                                 #calculate offset from rate
        fill = fill.crop((0, offset, 116, 100))                             #Crop fill image to the good size
        blank.paste(fill, (139, 70 + offset))                               #Paste fill image into the blank
        draw.text((140, 15), str(author), font=fnt, fill=red)               #Write author Name
        draw.text((140, 225), str(user), font=fnt, fill=red)                #Write user Name
        fnt = ImageFont.truetype("data/ship/font.ttf", 40)                  #Resize font
        draw.text((165, 96), str(rate) + "%", font=fnt, fill=white)         #Write rate %

        tmpl = Image.alpha_composite(tmpl, blank)                           #Merge template with blank
        tmpl.save("data/ship/tmp_ship.png", "PNG")                          #Save template to tmp file


    async def text_ship(self, author, user, rate):
        try:
            err = "I am sorry, but couldn't take a photo of both of you so I will give you text results:"
            msg = "**The Love rate between {0} and {1} is {2}%!**"
            b = discord.Embed(color = discord.Color(0xeb1818), title = err, description = msg.format(author, user, rate))
            await self.bot.say(embed=b)
        except errors.BadArgument:
            await self.bot.say("Oops, something went wrong! try again later!")

#Function to get the discord as a PIL image obj
def get_avatar(user):
    try:
        user_url, pic_size = str(user.avatar_url).split("?")                #Split to remove the image size
        response = requests.get(user_url + "?size=128", "r")                #URL request with Image at 128
        avatar = Image.open(io.BytesIO(response.content)).convert('RGBA')   #Open image in PLI
        tmp = Image.new('RGBA', avatar.size, (255, 255, 255, 255))          #Create white back ground
        tmp = Image.alpha_composite(tmp, avatar)                            #Merge avatar with a white background
        return (tmp)                                                        #Send the Image obj to parent function

    except:
        return (None)                                                       #Return None if can't get the avatar

def setup(bot):
    bot.add_cog(Ship(bot))
