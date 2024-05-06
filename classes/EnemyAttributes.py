from typing import Dict

class EnemyAttributes:
  def __init__(self, name, level, alignment, size, enemyType, additionalTags, perception, languages, skills, strength, dexterity,
              constitution,intelligence, wisdom, charisma, generalAbilities, items, armorClass, fortitudeSave, reflexSave, willSave,
              hitPoints, immunities, resistances, weaknesses, speed, strikes, spells, offensiveAbilities, enemyDescription):
    self.name = name
    self.level = level
    self.alignment = alignment
    self.size = size
    self.enemyType = enemyType
    self.additionalTags = additionalTags
    self.perception = perception
    self.languages = languages
    self.skills = skills
    self.strength = strength
    self.dexterity = dexterity
    self.constitution = constitution
    self.intelligence = intelligence
    self.wisdom = wisdom
    self.charisma = charisma
    self.generalAbilities = generalAbilities
    self.items = items
    self.armorClass = armorClass
    self.fortitudeSave = fortitudeSave
    self.reflexSave = reflexSave
    self.willSave = willSave
    self.hitPoints = hitPoints
    self.immunities = immunities
    self.resistances = resistances
    self.weaknesses = weaknesses
    self.speed = speed
    self.strikes = strikes
    self.spells = spells
    self.offensiveAbilities = offensiveAbilities
    self.enemyDescription = enemyDescription