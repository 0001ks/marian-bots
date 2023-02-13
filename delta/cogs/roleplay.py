import discord, requests, calendar, time, json
from discord.ext import commands
from discord.ui import Button, View
from pymongo import MongoClient
from pymongo.database import Database

class roleplay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db: Database = self.bot.cluster["test"]


    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kiss(self, ctx, *, member: discord.Member=None):
     if member == None:
        embed = discord.Embed(color=0xff0000, description=f"```ussage: kiss [member]```")
        await ctx.reply(embed=embed, mention_author=False)   
        return
     response = requests.get('http://api.nekos.fun:8080/api/kiss')
     data = response.json()
     embed = discord.Embed(color=0x2f3136, description=f"*Aww how cute! {ctx.author.mention} kissed {member.mention}*")
     embed.set_image(url=data["image"])
     await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cuddle(self, ctx, *, member: discord.Member=None):
     if member == None:
        embed = discord.Embed(color=0xff0000, description=f"```ussage: cuddle [member]```")
        await ctx.reply(embed=embed, mention_author=False) 
        return   
     response = requests.get('http://api.nekos.fun:8080/api/cuddle')
     data = response.json()
     embed = discord.Embed(color=0x2f3136, description=f"*Aww how cute! {ctx.author.mention} cuddled {member.mention}*")
     embed.set_image(url=data["image"])
     await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def hug(self, ctx, *, member: discord.Member=None):
     if member == None:
        embed = discord.Embed(color=0xff0000, description=f"```ussage: hug [member]```")
        await ctx.reply(embed=embed, mention_author=False) 
        return   
     response = requests.get('http://api.nekos.fun:8080/api/hug')
     data = response.json()
     embed = discord.Embed(color=0x2f3136, description=f"*Aww how cute! {ctx.author.mention} hugged {member.mention}*")
     embed.set_image(url=data["image"])
     await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def pat(self, ctx, *, member: discord.Member=None):
     if member == None:
        embed = discord.Embed(color=0xff0000, description=f"```ussage: pat [member]```")
        await ctx.reply(embed=embed, mention_author=False) 
        return   
     response = requests.get('http://api.nekos.fun:8080/api/pat')
     data = response.json()
     embed = discord.Embed(color=0x2f3136, description=f"*Aww how cute! {ctx.author.mention} pat {member.mention}*")
     embed.set_image(url=data["image"])
     await ctx.reply(embed=embed, mention_author=False)       

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def slap(self, ctx, *, member: discord.Member=None):
     if member == None:
        embed = discord.Embed(color=0xff0000, description=f"```ussage: slap [member]```")
        await ctx.reply(embed=embed, mention_author=False) 
        return   
     response = requests.get('http://api.nekos.fun:8080/api/slap')
     data = response.json()
     embed = discord.Embed(color=0x2f3136, description=f"*{ctx.author.mention} slapped {member.mention}*")
     embed.set_image(url=data["image"])
     await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def laugh(self, ctx):
     response = requests.get('http://api.nekos.fun:8080/api/laugh')
     data = response.json()
     embed = discord.Embed(color=0x2f3136, description=f"*{ctx.author.mention} laughs*")
     embed.set_image(url=data["image"])
     await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cry(self, ctx):
     response = requests.get('http://api.nekos.fun:8080/api/cry')
     data = response.json()
     embed = discord.Embed(color=0x2f3136, description=f"*{ctx.author.mention} cries*")
     embed.set_image(url=data["image"])
     await ctx.reply(embed=embed, mention_author=False)  

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def marry(self, ctx, *, member: discord.Member=None):
     if member == None:
       emb = discord.Embed(color=0x2f3136, title="marry", description="marry an user")
       emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
       emb.add_field(name="category", value="roleplay")
       emb.add_field(name="permissions", value="any")
       emb.add_field(name="usage", value="```marry [user]```", inline=False)
       emb.add_field(name="aliases", value="none")
       await ctx.reply(embed=emb, mention_author=False) 
       return
     elif member == ctx.author:
        embe = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} you can't marry yourself")
        await ctx.reply(embed=embe, mention_author=False) 
        return 
     elif member.bot:
        em = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} robots can't consent marriage")
        await ctx.reply(embed=em, mention_author=False)
        return     
     else:
       collection = self.db["marry"]
       ts = calendar.timegm(time.gmtime())  
       meri = collection.find_one({"_id": member.id})
       if meri is not None:
           await ctx.reply("uh oh! this user is already married!", mention_author=False)
           return
       else:
           mer = collection.find_one({"soulmate": member.id})
           if mer is not None:
               await ctx.reply("uh oh! this user is already married!", mention_author=False)
               return
                    
       check = collection.find_one({"_id": ctx.author.id})
       if check is not None:
           emb = discord.Embed(color=discord.Color.yellow(), description=f"{ctx.author.mention} you are already married. don't try to cheat!")
           await ctx.reply(embed=emb, mention_author=False)
           return
       else:
           check2 = collection.find_one({"soulmate": ctx.author.id})
           if check2 is not None:
             emb = discord.Embed(color=discord.Color.yellow(), description=f"{ctx.author.mention} you are already married. don't try to cheat!")
             await ctx.reply(embed=emb, mention_author=False)  
             return
           else:
             button1 = Button(label="yes", style=discord.ButtonStyle.green)
             button2 = Button(label="no", style=discord.ButtonStyle.red)
             embed = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} wants to marry you. do you accept?")
             async def button1_callback(interaction):
                 if interaction.user == ctx.author:
                     await interaction.response.send_message("you can't accept your own marriage", ephemeral=True)
                 elif interaction.user != member:
                     await interaction.response.send_message("you can't accept this", ephemeral=True)
                 else:                         
                  insert = {
                      "_id": ctx.author.id, "soulmate": member.id, "time": f"{ts}"
                  }
                  collection.insert_one(insert) 
                  embe = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} got married with {member.mention}")
                  await interaction.response.edit_message(content=None, embed=embe, view=None)       
             button1.callback = button1_callback  

             async def button2_callback(interaction):
                  if interaction.user == ctx.author:
                     await interaction.response.send_message("you can't accept your own marriage", ephemeral=True)
                  elif interaction.user != member:
                     await interaction.response.send_message("you can't accept this", ephemeral=True)
                  else:                         
                   embe = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} i'm sorry, but {member.mention} is probably not the right person for you")
                   await interaction.response.edit_message(content=None, embed=embe, view=None)
             button2.callback = button2_callback  

             marry = View()
             marry.add_item(button1)
             marry.add_item(button2)
             await ctx.send(f"{member.mention}", embed=embed, view=marry) 

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def divorce(self, ctx):
     collection = self.db["marry"]
     check = collection.find_one({"_id": ctx.author.id})
     if check is not None:
        button1 = Button(label="yes", style=discord.ButtonStyle.green)
        button2 = Button(label="no", style=discord.ButtonStyle.red)
        partner = check["soulmate"]
        embed = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} are you sure you want to divorce with <@{partner}>")
        async def button1_callback(interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("you can't interact with this message", ephemeral=True)
            else:
                collection.delete_one({"_id": ctx.author.id})
                emb = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} i'm sorry that you have decided to divorce")
                await interaction.response.edit_message(embed=emb, view=None)

        button1.callback = button1_callback

        async def button2_callback(interaction):
              if interaction.user != ctx.author:
                await interaction.response.send_message("you can't interact with this message", ephemeral=True)
              else:
                emb = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} alright you changed your mind")
                await interaction.response.edit_message(embed=emb, view=None)

        button2.callback = button2_callback

        divorce = View()
        divorce.add_item(button1)
        divorce.add_item(button2)
        await ctx.send(embed=embed, view=divorce)   
     elif check is None:
        check2 = collection.find_one({"soulmate": ctx.author.id})
        if check2 is not None:
             button3 = Button(label="yes", style=discord.ButtonStyle.green)
             button4 = Button(label="no", style=discord.ButtonStyle.red)
             partner = check2["_id"]
             embed = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} are you sure you want to divorce with <@{partner}>")
             async def button3_callback(interaction):
                if interaction.user != ctx.author:
                  await interaction.response.send_message("you can't interact with this message", ephemeral=True)
                else:
                  collection.delete_one({"_id": partner})
                  emb = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} i'm sorry that you have decided to divorce")
                  await interaction.response.edit_message(embed=emb, view=None)

             button3.callback = button3_callback

             async def button4_callback(interaction):
                if interaction.user != ctx.author:
                  await interaction.response.send_message("you can't interact with this message", ephemeral=True)
                else:
                  emb = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} alright you changed your mind")
                  await interaction.response.edit_message(embed=emb, view=None)

             button4.callback = button4_callback

             divorce2 = View()
             divorce2.add_item(button3)
             divorce2.add_item(button4)
             await ctx.send(embed=embed, view=divorce2)  
        elif check2 is None: 
            embe = discord.Embed(color=discord.Color.yellow(), description=f"{ctx.author.mention} you are not even married")
            await ctx.send(embed=embe)        

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def marriage(self, ctx, *, user: discord.User=None):
     if user == None:
        user = ctx.author

     collection = self.db["marry"]
     check = collection.find_one({"_id": user.id})
     if check is not None:
        time = check["time"]
        partner = check["soulmate"]
        embed = discord.Embed(color=0x2f3136, description = f"{user.mention} ❤️ <@{partner}>\n<t:{time}:R>")
        await ctx.reply(embed=embed, mention_author=False)
     else:
        check2 = collection.find_one({"soulmate": user.id})
        if check2 is not None:
           time = check2["time"]
           partner = check2["_id"]
           embed = discord.Embed(color=0x2f3136, description = f"{user.mention} ❤️ <@{partner}>\n<t:{time}:R>")
           await ctx.reply(embed=embed, mention_author=False)  
        else:
            embe = discord.Embed(color=0x2f3136, description=f"{user.mention} isn't even married")
            await ctx.reply(embed=embe, mention_author=False)         

async def setup(bot) -> None:
    await bot.add_cog(roleplay(bot))    
