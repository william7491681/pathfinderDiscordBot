import os
import typing
from dotenv import load_dotenv
from discord import Interaction, app_commands, File, Embed, Message, TextChannel, SelectOption, Thread
from discord.ui import Select, View
from classes.Bot import Bot
from encounters.Index import Encounters
from classes.ChooseEnemyType import ChooseEnemyTypeView, ChooseEnemySpecificTypeView
from classes.EncounterBuilder import EncounterBuilder
from html2image import Html2Image
from bs4 import BeautifulSoup as bs

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = Bot()
builder = EncounterBuilder()

def generateImage(htmlText: str, cssText: str, identifier: int):
  hti = Html2Image(output_path='views/', size=(800, 800))
  hti.screenshot(html_str=htmlText, css_str=cssText, save_as=f'statblock_numero_{identifier}.png')

# def editHtml(characterAttributes: json):
#   print()

@bot.event
async def on_message(message: Message):
  channel: TextChannel = message.channel
  if message.author != bot.user:
    await channel.send('User sent message')
    return
  if message.author == bot.user:
    # await channel.last_message.delete()
    if 'humanoid' in message.content.lower():
      builder.enemyType = 'Humanoid'
      ChooseEnemySpecificTypeView(builder)
      await channel.send('1 was chosen')
    if 'undead' in message.content.lower():
      await channel.send('2 was chosen')
    if 'animal' in message.content.lower():
      await channel.send('3 was chosen')
    if 'extraplanar' in message.content.lower():
      await channel.send('4 was chosen')
    if 'fey' in message.content.lower():
      await channel.send('5 was chosen')
    if 'monstrosity' in message.content.lower():
      await channel.send('6 was chosen')
    if 'primordial' in message.content.lower():
      await channel.send('7 was chosen')
    print(builder)

  channel: TextChannel = message.channel


@bot.tree.command()
async def enemy_generator(interaction: Interaction, option: typing.Literal[
  'Party Level: 1',
  'Party Level: 2',
  'Party Level: 3',
  'Party Level: 4',
  'Party Level: 5',
  'Party Level: 6',
  'Party Level: 7',
  'Party Level: 8',
  'Party Level: 9',
  'Party Level: 10',
  'Party Level: 11',
  'Party Level: 12',
  'Party Level: 13',
  'Party Level: 14',
  'Party Level: 15',
  'Party Level: 16',
  'Party Level: 17',
  'Party Level: 18',
  'Party Level: 19',
  'Party Level: 20'
]):
  channel = interaction.channel
  builder.partyLevel = int(option[-2:].strip())
  await interaction.response.send_message(option)
  await channel.send('', view=ChooseEnemyTypeView())

  # Call enemy generator class here
  # Mocking the enemy generator, returning two statblocks:
  # for i in range(2):
  #   with open('views/styles.css', 'r') as cssFile:
  #     if i == 0:
  #       with open('views/wight.html', 'r') as htmlFile:
  #         htmlText = htmlFile.read()
  #         cssText = cssFile.read()
  #         generateImage(htmlText, cssText, i)
  #     elif i == 1:
  #       with open('views/wight_copy.html', 'r') as htmlFile:
  #         htmlText = htmlFile.read()
  #         cssText = cssFile.read()
  #         generateImage(htmlText, cssText, i)

  #       # hti = Html2Image(output_path='views/', size=(800, 800))
  #       # await hti.screenshot(html_str=htmlText, css_str=cssText, save_as=f'statblock_numero_{i}.png')


  # if 'Humanoid' in option:
  #   # await interaction.response.send_message(f'Chose a humanoid: {option.split(sep=": ", )[1]}', ephemeral=True, )
  #   file1 = File('views/statblock_numero_0.png', filename='statblock_numero_0.png')
  #   file2 = File('views/statblock_numero_1.png', filename='statblock_numero_1.png')
  #   embed1 = Embed().set_image(url='attachment://statblock_numero_0.png')
  #   embed2 = Embed().set_image(url='attachment://statblock_numero_1.png')
  #   await interaction.response.send_message(content=f'Statblocks for {option}', files=[file1, file2], embeds=[embed1, embed2], ephemeral=True)

  # else:
  #   await interaction.response.send_message(f'chose {option}', ephemeral=True)

bot.run(token=TOKEN)