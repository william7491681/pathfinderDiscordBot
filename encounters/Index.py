import json
from .Humanoid import Humanoid

class Encounters:
  def __init__(self):
    self.humanoid = Humanoid()
    with open('./encounters/encounterTypes.JSON', 'r') as file:
      self.encounterTypes = json.load(file)['encounters']
      file.close()