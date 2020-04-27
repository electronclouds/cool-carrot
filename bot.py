# coolcarrot.py
import os
import random
import discord
import csv
from discord.ext import commands

coolcarrot = 'https://i.imgur.com/0QeqK7b.png'
TOKEN = 'NzA0MzE3MTA1MTY3NjYzMTU0.XqcQ9w.8_LXU1TxC5ks2l0j0spk-2IlgWk'

bot = commands.Bot(command_prefix='!')

@command.cooldown(1, 30, command.Bucketype.guild)
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
