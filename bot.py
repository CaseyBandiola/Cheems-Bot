# bot.py

import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

# Tell cheems to say something
@bot.command(name='cheems_say', help='Cheems will say what you want him to say.')
async def say(ctx, msg):
    response = cheemsify(msg)
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
            if isVowel(response[i][j]) and isConsonant(response[i][j+1]) and response[i][j+1] != 'm':
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
    return char.lower() in 'bcdfghjklmnpqrstvxzwy'

bot.run(TOKEN)
