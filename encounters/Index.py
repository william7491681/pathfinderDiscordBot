import json

class Encounters:
  def __init__(self):
    with open('./encounters/encounterTypes.JSON', 'r') as file:
      self.encounterTypes = json.load(file)['encounters']
      file.close()