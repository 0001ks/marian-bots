import discord, time, datetime, psutil
from discord.ext import commands
from discord.ui import View, Button, Select

global start

 
class info(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        global start
        start = time.time()

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def uptime(self, ctx):
        uptime = str(
            datetime.timedelta(seconds=int(round(time.time() - start))))
        e = discord.Embed(
            color=0x2f3136,
            description=f"**<a:zwhitebutterfly:1038394716435259412> Delta's uptime:** **{uptime}**")
        await ctx.reply(embed=e, mention_author=False)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.reply(f"<a:blackheartdrip_vcy:1038398349805625485> Pong :**`{round(self.bot.latency * 1000)}ms`**", mention_author=False)

    @commands.command(aliases = ['bi'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def botinfo(self, ctx):
        avatar_url = self.bot.user.avatar.url
        uptime = str(
            datetime.timedelta(seconds=int(round(time.time() - start))))
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count - 1

        embed = discord.Embed(
            color=0x2f3136,
            title=self.bot.user.name,
            description=
            "<:lord_reply3:1038157661860024392> <a:zwhitebutterfly:1038394716435259412> [Delta a multipurpose discord bot](https://discord.gg/xE2aFkj2cD)")
        embed.set_thumbnail(url=f'{avatar_url}')
        embed.add_field(
            name="<:lord_reply1:1038157657971900456> <a:zwhitebutterfly:1038394716435259412> Statistics",
            value=f"<:vamp_BlurpleCrown:1038397106907516948> Dev: **<@1009542636178247760>**\n<a:x_browser:1038398346462773288> Guilds: " + " ** "
            f"{len(self.bot.guilds)}" + "**\n<:users:1038394714401021972> Users: " + f"**{members}" +
            " ** \n<a:zwhitebutterfly:1038394716435259412> Discord.py Version: " + f" **{discord.__version__}**\n<a:x_sparkles:1038157515088744519> Ping: " +
            f"**{round(self.bot.latency * 1000)}ms**\n" +
            f"<:restart:1038394711586635776> Uptime: **{uptime}**\n<a:P_Saturn:1038157656646496297> Ram Usage: **{psutil.virtual_memory()[2]}%**"
        )
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def invite(self, ctx):
        embed = discord.Embed(
            color=0x2f3136,
            description="<:role:1038394709774708756> Add **Delta** a multi-purpose discord bot")
        embed.set_author(name=self.bot.user.name,
                         icon_url=self.bot.user.avatar.url)
        button1 = Button(label="support", url="https://discord.gg/xE2aFkj2cD")
        button2 = Button(
            label="invite",
            url=
            "https://discord.com/oauth2/authorize?client_id=1014050243328888894&permissions=8&scope=bot%20applications.commands"
        )
        view = View()
        view.add_item(button1)
        view.add_item(button2)
        await ctx.reply(embed=embed, view=view, mention_author=False)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def help(self, ctx):
        embed = discord.Embed(color=0x2f3136, description="")
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_author(name="help panel", icon_url=self.bot.user.avatar.url)
        embed.add_field(name="<:lord_reply3:1038157661860024392> <a:vrn_blackdot:1038396039989825616> Commands",
                        value="<a:zwhitebutterfly:1038394716435259412> Use the dropdown menu below to see commands",
                        inline=False)
        embed.add_field(
            name="<:emoji_52:1043791077980782632><a:vrn_blackdot:1038396039989825616> Support",
            value=
            "<a:zwhitebutterfly:1038394716435259412> If you need support contact us in the [support server](https://discord.gg/xE2aFkj2cD)"
        )
        button1 = Button(label="support", url="https://discord.gg/xE2aFkj2cD")
        button2 = Button(
            label="invite",
            url=
            f"https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot%20applications.commands"
        )
        select = Select(
            placeholder="select category",
            options=[
                discord.SelectOption(label="home"),
                discord.SelectOption(label="config"),
                discord.SelectOption(label="info"),
                discord.SelectOption(label="utility"),
                discord.SelectOption(label="moderation"),
                discord.SelectOption(label="roleplay"),
                discord.SelectOption(label="lastfm"),
                discord.SelectOption(label="emoji"),
                discord.SelectOption(label="countdowns")
                
            ])

        async def select_callback(interaction: discord.Interaction):
            if interaction.user != ctx.author:
                em = discord.Embed(
                    color=0xffff00,
                    description=f"<:check_warning:1023193803877785710> {interaction.user.mention} you are not the author of this message"
                )
                await interaction.response.send_message(embed=em, ephemeral=True)
                return
           

            if select.values[0] == "home":
                await interaction.response.edit_message(embed=embed)
            elif select.values[0] == "info":
                e = discord.Embed(color=0x2f3136, title="info commands")
                e.set_thumbnail(url=self.bot.user.avatar.url)
                e.add_field(name="info",
                            value="`botinfo , ping , uptime , mods , vanity , vote`",
                            inline=False)   
                await interaction.response.edit_message(embed=e)
            elif select.values[0] == "utility":
                e = discord.Embed(color=0x2f3136,
                                  title="utility Commands")
                e.set_thumbnail(url=self.bot.user.avatar.url)
                e.add_field(name="utility",
                            value="`server , userinfo , banner , avatar , template , boostcount , reactionsnipe , membercount , tags , server banner , server icon , clear , invites , webshot , roles`",
                            inline=False) 
                await interaction.response.edit_message(embed=e)
            elif select.values[0] == "moderation":
                e = discord.Embed(color=0x2f3136, title="moderation commands")
                e.set_thumbnail(url=self.bot.user.avatar.url)
                e.add_field(name="moderation", value="`kick , ban , unban , autoresponder , nickset , role`", inline=False)
                await interaction.response.edit_message(embed=e)
            elif select.values[0] == "roleplay":
                e = discord.Embed(color=0x2f3136,
                                  title="roleplay commands")
                e.set_thumbnail(url=self.bot.user.avatar.url)
                e.add_field(name="roleplay",
                            value="`hug , marriage , divorce , kiss , slap , cuddle , marry , pat , cry , laugh`",
                            inline=False)
                await interaction.response.edit_message(embed=e)
            elif select.values[0] == "lastfm":
                e = discord.Embed(color=0x2f3136,
                                  title="lastfm commands")
                e.set_thumbnail(url=self.bot.user.avatar.url)
                e.add_field(name="lastfm",
                            value="`lastfm , lastfm set , lastfm customcommand , lastfm embed , nowplaying`",
                            inline=False)
                await interaction.response.edit_message(embed=e)
            elif select.values[0] == "countdowns":
                e = discord.Embed(color=0x2f3136, title="countdowns commands")
                e.set_thumbnail(url=self.bot.user.avatar.url)
                e.add_field(name="countdowns", value="`xmas , summer , newyear`", inline=False)
                await interaction.response.edit_message(embed=e)
            elif select.values[0] == "emoji":
                e = discord.Embed(color=0x2f3136, title="emoji commands")
                e.set_thumbnail(url=self.bot.user.avatar.url)
                e.add_field(name="emoji", value="`steal`", inline=False)
                await interaction.response.edit_message(embed=e)
            elif select.values[0] == "config":
                    e = discord.Embed(color=0x2f3136, title="config commands")
                    e.add_field(name="config",value="`autoresponder`",inline=False)
                    await interaction.response.edit_message(embed=e)

        select.callback = select_callback 

        view = View()
        view.add_item(select)
        view.add_item(button1)
        view.add_item(button2)
        

        await ctx.reply(embed=embed, view=view, mention_author=False)  
        
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def template(self, ctx):
        embed = discord.Embed(color=0x2f3136, description="")
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_author(name="Template Selecter", icon_url=self.bot.user.avatar.url)
        embed.add_field(name="Choose",
                        value="**Use the dropdown menu below to choose a template to copy**",
                        inline=False)
        embed.add_field(
            name="info",
            value=
            "**The bot recomande you a template the bot will dont load a template/save**"
        )
        button4 = Button(label="support", url="https://discord.gg/xE2aFkj2cD")
        button3 = Button(
            label="invite",
            url=
            f"https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot%20applications.commands"
        )
        select = Select(
            placeholder="select category",
            options=[
                discord.SelectOption(label="home"),
                discord.SelectOption(label="community")
                
            ])

        async def select_callback(interaction: discord.Interaction):
            if interaction.user != ctx.author:
                em = discord.Embed(
                    color=0xffff00,
                    description=
                    f"<:check_warning:1023193803877785710> {interaction.user.mention} you are not the author of this message"
                )
                await interaction.response.send_message(embed=em, ephemeral=True)
                return
           

            if select.values[0] == "home":
                await interaction.response.edit_message(embed=embed)
            elif select.values[0] == "community":
                e = discord.Embed(color=0x2f3136,
                                  title="Community Templates")
                e.set_thumbnail(url=self.bot.user.avatar.url)
                e.add_field(name="Delta",
                            value="**<:1_vcy:1030446438645235752> : https://discord.new/KH5dDkawVTaA**\n**<:2_1:1030446441522532362> : https://discord.new/YWqCyacWn5AK **",
                            inline=False) 
                await interaction.response.edit_message(embed=e)
            
        select.callback = select_callback 

        view = View()
        view.add_item(select)
        view.add_item(button4)
        view.add_item(button3)
        

        await ctx.reply(embed=embed, view=view, mention_author=False)

async def setup(bot) -> None:
    await bot.add_cog(info(bot))
