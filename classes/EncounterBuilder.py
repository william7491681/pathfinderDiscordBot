class EncounterBuilder:
  def __init__(self, partyLevel: int = None, enemyType: str = None, specificEnemyType: str = None):
    self.partyLevel = partyLevel,
    self.enemyType = enemyType
    self.specificEnemyType = specificEnemyType

  def __str__(self):
    return f'Party Level: {self.partyLevel}, Enemy Type: {self.enemyType}, Specific Enemy Type: {self.specificEnemyType}'