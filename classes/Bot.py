from discord.ext import commands
from discord import Intents

intents = Intents()
intents.message_content = True

class Bot(commands.Bot):
  def __init__(self):
    super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=intents)

  async def on_ready(self):
    await self.tree.sync()
    print(f'{self.user} is running!')