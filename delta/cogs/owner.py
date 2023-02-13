import discord
from discord.ext import commands
import random
from typing import Union, Optional

class owner(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot
    
async def setup(bot) -> None:
    await bot.add_cog(owner(bot))