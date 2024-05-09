from discord import SelectOption, Interaction
from discord.ui import Select, View
from .EncounterBuilder import EncounterBuilder
from encounters.Index import Encounters

class ChooseNumberOfPlayersSelect(Select):
    def __init__(self, builder: EncounterBuilder, options=None):
        self.builder = builder
        super().__init__(placeholder="Select the number of players in the party", max_values=1, min_values=1, options=options)
    async def callback(self, interaction: Interaction):
        self.builder.numPlayers = int(self.values[0])
        await interaction.channel.last_message.delete()
        await interaction.response.send_message('', view=ChooseEnemyTypeView(self.builder))

class ChooseNumberOfPlayersView(View):
    def __init__(self, builder: EncounterBuilder, *, timeout=180):
        super().__init__(timeout=timeout)
        selectOptions = [
            SelectOption(label='', emoji='1️⃣'),
            SelectOption(label='', emoji='2️⃣'),
            SelectOption(label='', emoji='3️⃣'),
            SelectOption(label='', emoji='4️⃣'),
            SelectOption(label='', emoji='5️⃣'),
            SelectOption(label='', emoji='6️⃣'),
            SelectOption(label='', emoji='7️⃣'),
            SelectOption(label='', emoji='8️⃣'),
        ]
        self.add_item(ChooseNumberOfPlayersSelect(builder, selectOptions))

class ChooseEnemyTypeSelect(Select):
    def __init__(self, builder: EncounterBuilder, options=None):
        self.builder = builder
        super().__init__(placeholder="Select an enemy type",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: Interaction):
        self.builder.enemyType = self.values[0]
        await interaction.channel.last_message.delete()
        await interaction.response.send_message('', view=ChooseEnemySpecificTypeView(self.builder))

class ChooseEnemyTypeView(View):
    def __init__(self, builder: EncounterBuilder, *, timeout=180):
        self.builder = builder
        super().__init__(timeout=timeout)
        selectOptions=[
            SelectOption(label="Humanoid", emoji="🧍"),
            SelectOption(label="Undead", emoji="🧟"),
            SelectOption(label="Animal", emoji="🐯"),
            SelectOption(label="Extraplanar", emoji="😈"),
            SelectOption(label="Fey", emoji="🧚"),
            SelectOption(label="Monstrosity", emoji="👹"),
            SelectOption(label="Primordial", emoji="🐲"),
            ]
        self.add_item(ChooseEnemyTypeSelect(builder, selectOptions))

class ChooseEnemySpecificTypeSelect(Select):
    def __init__(self, builder: EncounterBuilder, options=None):
        self.builder = builder
        super().__init__(placeholder='Select up to 4 specific enemy types in the encounter', max_values=4, min_values=1, options=options)
    async def callback(self, interaction: Interaction):
        self.builder.specificEnemyType = self.values
        await interaction.channel.last_message.delete()
        await interaction.response.send_message('', view=ChooseDifficultyView(self.builder))

class ChooseEnemySpecificTypeView(View):
    def __init__(self, builder: EncounterBuilder, *, timeout=180):
        super().__init__(timeout=timeout)
        encounters = Encounters()
        selectOptions = [SelectOption(label='Random (only select this for random generation)')]
        if builder.enemyType == 'Humanoid':
            for specificEnemyType in encounters.encounterTypes['Humanoid']:
                selectOptions.append(SelectOption(label=specificEnemyType))
        self.add_item(ChooseEnemySpecificTypeSelect(builder, selectOptions))

class ChooseDifficultySelect(Select):
    def __init__(self, builder: EncounterBuilder, options=None):
        self.builder = builder
        super().__init__(placeholder='Select a difficulty for the encounter', max_values=1, min_values=1, options=options)
    async def callback(self, interaction: Interaction):
        self.builder.difficulty = self.values[0]
        await interaction.channel.last_message.delete()
        self.builder.generateEncounter()

class ChooseDifficultyView(View):
    def __init__(self, builder: EncounterBuilder, *, timeout=180):
        super().__init__(timeout=timeout)
        selectOptions = [
            SelectOption(label='Trivial', emoji='🟢'),
            SelectOption(label='Low', emoji='🟡'),
            SelectOption(label='Moderate', emoji='🟠'),
            SelectOption(label='Severe', emoji='🔴'),
            SelectOption(label='Extreme', emoji='⚫'),
        ]
        self.add_item(ChooseDifficultySelect(builder, selectOptions))