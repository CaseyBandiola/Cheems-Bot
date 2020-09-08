# Cheems-Bot
I just did this for fun. This is the code for a Cheems Bot in Discord.

# Commands
```
  $cheems-say "....."
```
  - Cheems will iterate through each word of the input string
  - Cheems looks at the first instance of a vowel and consonant combination, with the additional constraint that the consonant is not the letter 'm'
  - Cheems inserts an 'm' in between the vowel and consonant
  
```
  $cheems-be-wholesome
```
  - Cheems will randomly say something wholesome from a number of responses
  - There are 6 preset wholesome responses

```
  $cheems-sleep
```
  - CheemsBot will send a short goodbye message and then disonnect from the Discord server

```
   $cheems-king
```
  - CheemsBot will send a photo named "king.jpg" if it exists in the same directory
  - If no image exists, CheemsBot will not do anything
  - The image has to be in the same directory as bot.py when it is ran