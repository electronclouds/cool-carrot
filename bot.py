# coolcarrot.py
import os
import random
import discord
import csv
from discord.ext import commands

coolcarrot = 'https://i.imgur.com/0QeqK7b.png'
TOKEN = 'API-KEY'

bot = commands.Bot(command_prefix='!')

@bot.command(name='motivate')
async def bloomer(ctx):
  picture = discord.Embed()
  picture.set_image(url=coolcarrot)
  with open('./cool.csv') as quote:
   quoteread = csv.reader(quote, delimiter=',')
   quotelist = list(quoteread)
   row = random.randrange(1,10)
   response = quotelist[row][0]
   await ctx.send(embed = picture)
   await ctx.send(response)

bot.run(TOKEN)
