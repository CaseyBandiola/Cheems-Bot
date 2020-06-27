# bot.py

import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

# Shows that Cheems is online
@bot.event
async def on_ready():
    print(f'{bot.user.name} is online!')

# Tell cheems to say something
@bot.command(name='cheems-say', help='Cheems will say what you want him to say.')
async def say(ctx, msg):
    response = cheemsify(msg)
    await ctx.send(response)

# Tell cheems to say something wholesome
@bot.command(name='cheems-be-wholesome', help='Cheems will say something wholesome.')
async def wholesome(ctx):
    wholesome_quotes = [
        cheemsify("I love you"),
        cheemsify("You matter"),
        cheemsify("Have a nice day"),
        cheemsify("Don't forget to drink water today"),
        cheemsify("Did you eat enough today?"),
        cheemsify("Hope you have a good day!"),
    ]

    response = random.choice(wholesome_quotes)
    await ctx.send(response)

# Cheemsifies the message
def cheemsify(msg):
    response = msg.split()
    returnmsg = ""

    # iterate through each word in the message
    for i in range(len(response)):
        # iterate through the word
        # if word is less than or equal to 3 letters, skip it
        if len(response[i]) <= 3:
            if i != len(response) - 1:
                returnmsg += response[i] + " "
            else:
                returnmsg += response[i]
            continue
        # otherwise, cheemsify the word
        for j in range( len(response[i])-1 ):
            if isVowel(response[i][j]) and isConsonant(response[i][j+1]):
                new_word = response[i][:j+1]+"m"+response[i][j+1:]
                response[i] = new_word
                break

        if i != len(response) - 1:
            returnmsg += response[i] + " "
        else:
            returnmsg += response[i]

    return returnmsg

def isVowel(char):
    return char.lower() in 'aeiou'

def isConsonant(char):
    return char.lower() in 'bcdfghjklnpqrstvxzwy'

# error handling for say()
@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.send('I canm\'t say thamt')

bot.run(TOKEN)
