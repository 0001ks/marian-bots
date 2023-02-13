import discord, datetime, time, psutil
from typing import Union
from discord import app_commands
from discord.ext import commands

global startTime

class slash(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        global startTime
        startTime = time.time()
        
    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        print(f'synced {len(fmt)} commands to guilds')
        await ctx.message.add_reaction("<a:check_yes:1022917129953083452>")   
        return
  
    @app_commands.command(name="help", description="help command")
    async def help(self, interaction: discord.Interaction):
        e = discord.Embed(color=0x2f3136, description=f"<@{interaction.user.id}> my prefix is `*`")
        await interaction.response.send_message(embed=e)
        
    @app_commands.command(name="ping", description="ping command")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"**Delta ping : ** `{round(self.bot.latency * 1000)}ms`")
        
    @app_commands.command(name="uptime", description="uptime command")
    async def uptime(self, interaction: discord.Interaction):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        e = discord.Embed(color=0x2f3136, description=f"**{self.bot.user.name}'s** uptime: **{uptime}**")
        await interaction.response.send_message(embed=e)

async def setup(bot):
    await bot.add_cog(slash(bot))
