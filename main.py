import discord
import datetime
import random


token = "봇 토큰"

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

years_ = ['2017','2018']

텍스트 = ["계좌 문의 드립니다.","계좌 있으신가요?"]

@client.event 
async def on_member_join(member):
    date = datetime.datetime.utcfromtimestamp(((int(member.id) >> 22) + 1420070400000) / 1000)
    random_name = random.randint(1000, 9999)
    if date.year in years_ or member.name == random_name:
            await member.send("당신은 경찰 의심 대상으로 확정 되었음으로 서버에서 추방 되었습니다!")
            await member.kick(reason='경찰 의심 대상')
    else:
        await member.send("당신은 경찰 의심 조사에서 피해갔습니다!")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name= f"경찰 추방 봇", url="https://www.twitch.tv/whitehole"))


client.run(token)        
