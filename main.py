import os
import typing
from dotenv import load_dotenv
from discord import Interaction, app_commands, File, Embed, Message, TextChannel
from discord.ui import Select
from classes.Bot import Bot
from encounters.Index import Encounters
from html2image import Html2Image
from bs4 import BeautifulSoup as bs

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = Bot()

def generateImage(htmlText: str, cssText: str, identifier: int):
  hti = Html2Image(output_path='views/', size=(800, 800))
  hti.screenshot(html_str=htmlText, css_str=cssText, save_as=f'statblock_numero_{identifier}.png')

# def editHtml(characterAttributes: json):
#   print()

@bot.event
async def on_message(message: Message):
  if message.author != bot.user:
    Select(placeholder='Select an option', options=[app_commands.Choice(name='Humanoid: Goblin', value='Humanoid: Goblin')])
    return
  if message.author == bot.user:
    if (message.content != 'How many players are in the party?') or (message.content != 'What level are the party members?'):
      return

  channel: TextChannel = message.channel
  await channel.last_message.add_reaction('1️⃣')
  await channel.last_message.add_reaction('2️⃣')
  await channel.last_message.add_reaction('3️⃣')
  await channel.last_message.add_reaction('4️⃣')

  async def check(reaction, user):
    print(reaction)
    print(reaction.emoji)
    if (str(reaction.emoji) == '4️⃣'):
      return True
    else:
      return False

  try:
    reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
    if str(reaction.emoji) == '2️⃣':
      await channel.last_message.delete()
      await channel.send('What level are the party members?')
  except:
    await channel.send('Did not respond in time')
  else:
    None


@bot.tree.command()
async def enemy_generator(interaction: Interaction, option: str):
  # Call enemy generator class here
  # Mocking the enemy generator, returning two statblocks:
  await interaction.channel.send('How many players are in the party?')
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

  interaction.response.send_modal()


  # if 'Humanoid' in option:
  #   # await interaction.response.send_message(f'Chose a humanoid: {option.split(sep=": ", )[1]}', ephemeral=True, )
  #   file1 = File('views/statblock_numero_0.png', filename='statblock_numero_0.png')
  #   file2 = File('views/statblock_numero_1.png', filename='statblock_numero_1.png')
  #   embed1 = Embed().set_image(url='attachment://statblock_numero_0.png')
  #   embed2 = Embed().set_image(url='attachment://statblock_numero_1.png')
  #   await interaction.response.send_message(content=f'Statblocks for {option}', files=[file1, file2], embeds=[embed1, embed2], ephemeral=True)

  # else:
  #   await interaction.response.send_message(f'chose {option}', ephemeral=True)


@enemy_generator.autocomplete('option')
async def enemy_generator_autocompletion(interaction: Interaction, currentInput: str) -> typing.List[app_commands.Choice[str]]:
  data = []

  encounters = Encounters().encounterTypes
  for encounter in encounters:
    if len(data) >= 25:
      break
    if currentInput.lower() in encounter.lower():
      data.append(app_commands.Choice(name=encounter, value=encounter))
  return data

bot.run(token=TOKEN)