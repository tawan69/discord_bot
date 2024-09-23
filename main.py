import os
import discord
from discord.ext import commands
from discord import app_commands
from myserver import server_on


# แก้ไข command_prefix
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# bot Event
# คำสั่ง bot พร้อมใช้งาน
@bot.event
async def on_ready():
    print(f"Bot Online!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")



# แจ้งคนเข้า - คนออกเซิฟเวอร์
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1286658303983616080) # ID ห้อง
    text = f"Welcome to the server, {member.mention}!" # ข้อความที่ต้องการ
    
    emmbed = discord.Embed(title = 'ยินดีต้อนรับเจ้าหน้าใหม่',
                           description = text ,
                           color = 0x3b285a)
    
    await channel.send(embed = emmbed) # ส่งข้อความห้อง
    await member.send(embed = emmbed) # ส่งข้อความส่วนตัว



@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1286727588299018270) # ID ห้อง
    text = f"{member.mention} has left the server!"
    
    emmbed = discord.Embed(title = 'ช่างน่าเสียดาย',
                           description = text ,
                           color = 0xcd384f)
    
    await channel.send(embed = emmbed) # ส่งข้อความห้อง



# คำสั่ง chatbot
@bot.event
async def on_message(message):
    mes = message.content.lower()  # บอทสามารถตรวจสอบคำทักทายได้โดยไม่คำนึงถึงการใช้ตัวพิมพ์ใหญ่หรือตัวพิมพ์เล็ก

    # การจัดการภาษาอังกฤษ
    if mes in ["'hello', 'hi', 'hey there'"]:
        await message.channel.send("Hello")
        
    elif mes in ["what's up", "how's it going"]:
        await message.channel.send("I'm good")

    elif mes in ['good morning', 'good afternoon', 'good evening']:
        await message.channel.send("Good to see you")

    elif mes in ['hello bot', 'hi bot', 'hibot', 'hellobot', 'hi_bot', 'hello_bot']:
        await message.channel.send("Hello " + str(message.author.name) + " Nice to see you")

    # การจัดการภาษาไทย
    elif mes in ['สวัสดี', 'หวัดดี', 'เฮ้']:
        await message.channel.send("สวัสดีครับ")
    
    elif mes in ['เป็นไงบ้าง', 'สบายดีไหม']:
        await message.channel.send("สบายดีครับ")

    elif mes in ['สวัสดีตอนเช้า', 'สวัสดีตอนบ่าย', 'สวัสดีตอนเย็น']:
        await message.channel.send("ดีใจที่ได้เจอครับ")
        
    elif mes in ['สวัสดีบอท', 'หวัดดีบอท']:
        await message.channel.send("สวัสดี " + str(message.author.name) + " ดีใจที่ได้เจอครับ")
        

# /////////////////////////////////// Commands ///////////////////////////////////
# กำหนดคำสั่งให้บอท      
@bot.tree.command(name='hibot', description='w Hello')
async def hi(interaction):
    await interaction.response.send_message('Hello w')

@bot.tree.command(name='name')
@app_commands.describe(name = "What's your name?")
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"Hello {name}")
    
@bot.tree.command(name='hp', description='Bot Commands')
async def hpCommands(interaction):
    emmbed = discord.Embed(title='hp - Bot Commands',
                            description ='Bot Commands',
                            color = 0xcd384f,
                            timestamp = discord.utils.utcnow())
    
    embed.add_field(name='/hello', value='HelloCommands', inline=False)
    await interaction.response.send_message(embed = emmbed)


server_on()

# รันบอทด้วยโทเค็น
bot.run(os.getenv('TOKEN'))
