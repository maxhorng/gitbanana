#導入 Discord.py
import discord
#client 是我們與 Discord 連結的橋樑
client = discord.Client()

#調用 event 函式庫
@client.event   
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('StreetFighterV')
    await client.change_presence(status=discord.Status.idle, activity=game)
@client.event
#當有訊息時

async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #如果包含 ，機器人回傳 
    if message.content.startswith('我想問'):
        role1 = message.guild.get_role(993621670738804867)#資工
        role2 = message.guild.get_role(993621719904419910)#資傳
        role3 = message.guild.get_role(993621670738804867)#
        role4 = message.guild.get_role(993621719904419910)#
        role5 = message.guild.get_role(993621670738804867)#
        role6 = message.guild.get_role(993621719904419910)#
        role7 = message.guild.get_role(993621670738804867)#
        role8 = message.guild.get_role(993621719904419910)#
        role9 = message.guild.get_role(993621670738804867)#
        role10 = message.guild.get_role(993621719904419910)#
        role11 = message.guild.get_role(993621670738804867)#
        role12 = message.guild.get_role(993621719904419910)#
        role13 = message.guild.get_role(993621670738804867)#
        role14 = message.guild.get_role(993621719904419910)#
        role15 = message.guild.get_role(993621670738804867)#
        role16 = message.guild.get_role(993621719904419910)#
        role17 = message.guild.get_role(993621670738804867)#
        role18 = message.guild.get_role(993621719904419910)#
        role19 = message.guild.get_role(993621670738804867)#
        role20 = message.guild.get_role(993621719904419910)#
        role21 = message.guild.get_role(993621670738804867)#
        role22 = message.guild.get_role(993621719904419910)#
        role23 = message.guild.get_role(993621670738804867)#
        role24 = message.guild.get_role(993621719904419910)#

        author= message.author
        outrole=''
        
        if role1 in message.author.roles:
            outrole='資工提問'

        elif role2 in message.author.roles:
            outrole='資管提問'
        
        await message.delete()
        await message.channel.send("["+outrole+"]"+message.author.mention+message.content) #"@%s",message.author.id,
        
        
        

client.run('OTkzMjgwOTkxMDA5NDQ4MDE2.Giwol3.5vIpxNnhkfzvU6Xi-tYruskgG6-5alRw12teNw') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面