import discord, os, requests, json
from tasty import requestData, sortRecipeData,sortText

TOKEN = 'MTAwOTU0MTY4MjE2NzA0MjA5OQ.GM17jk.FivMgFEvuPaODHeVEP279A30ZeRQCinhqAx__E'

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return 
    
  if message.content.startswith('!Tastybot info'):
     await message.channel.send('Type "!Tastybot *recipename* *#recipes*" ')
    
  if message.content.startswith('!Tastybot'):
    print(message.content[10:])
    command = message.content[10:]
    info = sortText(sortRecipeData(requestData(command,5)))[0]
    
    #await message.channel.send(message.content[8:])
    await message.channel.send(info)

#client.run(os.getenv('TOKEN'))
client.run(TOKEN)