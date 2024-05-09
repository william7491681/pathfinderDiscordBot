class EncounterBuilder:
  def __init__(self, numPlayers: int = None, partyLevel: int = None, enemyType: str = None, specificEnemyType: str = None, difficulty: int = None):
    self.numPlayers = numPlayers,
    self.partyLevel = partyLevel,
    self.enemyType = enemyType
    self.specificEnemyType = specificEnemyType
    self.difficulty = difficulty

  def __str__(self):
    return f'Party Level: {self.partyLevel}, Enemy Type: {self.enemyType}, Specific Enemy Type: {self.specificEnemyType}, Difficulty: {self.difficulty}'

  def generateEncounter(self):
    print(f'Generating encounter statblocks based off of data:\n{self}')