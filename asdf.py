from bs4 import BeautifulSoup as bs
from classes.EnemyAttributes import EnemyAttributes

def main():
  with open('./views/wight.html') as file:
    soup = bs(file, 'html.parser')

  name = soup.find(id='name')
  level = soup.find(id='level')
  alignment = soup.find(id='alignment')
  size = soup.find(id='size')
  enemyType = soup.find(id='enemyType')
  additionalTags = soup.find(id='additionalTagsWrapper')
  parsedAdditionalTags = []
  for i in additionalTags:
    if i != '\n':
      parsedAdditionalTags.append(i.text.strip())
  perception = soup.find(id='perception')
  senses = soup.find(id='senses')
  languages = soup.find(id='languages')
  skills = soup.find(id='skillsWrapper')
  parsedSkills = []
  for i in skills.find_all('span'):
    i: bs = i
    if i.contents != '\n':
      i = str(i.text).replace(u'\xa0', u' ').strip()
      parsedSkills.append(i)
  strScore = soup.find(id='strScore')
  dexScore = soup.find(id='dexScore')
  conScore = soup.find(id='conScore')
  intScore = soup.find(id='intScore')
  wisScore = soup.find(id='wisScore')
  chaScore = soup.find(id='chaScore')
  generalAbilities = soup.find(id='generalAbilitiesWrapper')
  items = soup.find(id='itemsWrapper')
  armorClass = soup.find(id='armorClass')
  fortSave = soup.find(id='fortSave')
  refSave = soup.find(id='refSave')
  willSave = soup.find(id='willSave')
  hitPoints = soup.find(id='hitPoints')
  immunities = soup.find(id='immunities')
  resistances = soup.find(id='resistances')
  weaknesses = soup.find(id='weaknesses')
  speed = soup.find(id='speed')
  strikes = soup.find(id='strikes')
  spells = soup.find(id='spells')
  offensiveAbilities = soup.find(id='offensiveAbilitiesWrapper')
  enemyDescription = soup.find(id='enemyDescription')

  # print('name: ', name.text)
  # print('level: ', level.text)
  # print('alignment: ', alignment.text)
  # print('size: ', size.text)
  # print('enemyType: ', enemyType.text)
  # print('additionalTags: ', parsedAdditionalTags)
  # print('perception: ', perception.text)
  # print('senses: ', senses.text)
  # print('languages: ', languages.text)
  # print('skills: ', parsedSkills)
  # print('strScore: ', strScore.text)
  # print('dexScore: ', dexScore.text)
  # print('conScore: ', conScore.text)
  # print('intScore: ', intScore.text)
  # print('wisScore: ', wisScore.text)
  # print('chaScore: ', chaScore.text)
  # print('generalAbilities: ', generalAbilities.contents)
  # for i in generalAbilities.find_all(id="generalAbility"):
  #   i: bs = i
  #   print(i.find(id='generalAbilityDescription'))
  # print('items: ', items.contents)
  # print('armorClass: ', armorClass.text)
  # print('fortSave: ', fortSave.text)
  # print('refSave: ', refSave.text)
  # print('willSave: ', willSave.text)
  # print('hitPoints: ', hitPoints.text)
  # print('immunities: ', immunities.text)
  # print('resistances: ', resistances.text)
  # print('weaknesses: ', weaknesses.text)
  # print('speed: ', speed.text)
  # print('strikes: ', strikes)
  # print('spells: ', spells.text)
  # print('offensiveAbilities: ', offensiveAbilities.contents)
  # print('enemyDescription: ', enemyDescription.text)

  # test = EnemyAttributes(

  # )

main()