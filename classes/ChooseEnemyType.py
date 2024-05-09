from discord import SelectOption, Interaction
from discord.ui import Select, View

class ChooseEnemyTypeSelect(Select):
    def __init__(self, options=None):
        super().__init__(placeholder="Select an enemy type",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: Interaction):
        await interaction.channel.last_message.delete()
        await interaction.response.send_message(content=f"Your choice is {self.values[0]}!")

class ChooseEnemyTypeView(View):
    def __init__(self, *, timeout=180):
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
        self.add_item(ChooseEnemyTypeSelect(options=selectOptions))

class ChooseEnemySpecificTypeSelect(Select):
    def __init__(self, options=None):
        super().__init__(placeholder='Select specific enemy type', max_values=1, min_values=1, options=options)
    async def callback(self, interaction: Interaction):
        await interaction.channel.last_message.delete()
        await interaction.response.send_message(content=f'Your choice is {self.values[0]}!')

class ChooseEnemySpecificTypeView(View):
    def __init__(self, builder, *, timeout=180):
        super().__init__(timeout=timeout)
        self.add_item(ChooseEnemySpecificTypeSelect(options=selectOptions) )