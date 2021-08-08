import discord
import os
from discord.ext import tasks, commands
from discord import Webhook, RequestsWebhookAdapter
from discord_slash import SlashCommand, SlashContext
import keep_alive
from discord.ext.commands import BotMissingPermissions
import json
import random
from urllib.request import urlopen
import asyncio 
import datetime
import requests
import math
from datetime import datetime
import giphy_client
import personalmodules as pm
from pygicord import Paginator
import pytz
import time
from discord import Spotify
import re
from bs4 import BeautifulSoup

colour = [0xDC143C, 0xD35400, 0x48C9B0, 0x7FB3D5, 0xffa0a2]

#ist = pytz.timezone('Asia/Calcutta')
#today = (datetime.now(ist))
#print('Month:', today.month)
#print('Day :', today.day)

intents = discord.Intents(
messages=True, guilds=True, reactions=True, members=True)
client = commands.Bot(command_prefix = "f", intents=intents, allowed_mentions=discord.AllowedMentions(replied_user=False))
client.remove_command("help")

@client.command()
async def factorial(ctx, num:int):
    await ctx.send(math.factorial(num))
@client.command()
async def calc(ctx, *, stuff):
    stuff = stuff.replace("\\", "")
    stuff = stuff.replace("(", "*(")
    exec(f"print({stuff})\na = {stuff}\nprint(a)\nwith open('calc.txt', 'w') as f:\n    f.write(str(a))")
    with open("calc.txt", "r") as f:
        data = f.readlines()
    await ctx.send(data[0])

@client.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, BotMissingPermissions):
        await ctx.send(":redTick: You Are Missing Perms")
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(f"The Command is currently on cooldown. Please try again in {int(error.retry_after)} seconds")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send('Please pass all the required arguments')
        
#date1 = (str(f"{today.day}-{today.month}"))

#sorry by i had copied this command's code from somewhere becuz i was too lazy to write this thing....it's easy tho...if i get time, i'll make my own version of this and upload it...i can't remember the source rn
@client.command(case_insensitive = True, aliases = ["remind", "remindme", "remind_me"])
@commands.bot_has_permissions(attach_files = True, embed_links = True)
async def reminder(ctx, time, *, reminder):
    print(time)
    print(reminder)
    user = ctx.message.author
    embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
    embed.set_footer(text="If you have any questions, suggestions or bug reports, please join our support Discord Server: link hidden", icon_url=f"{client.user.avatar_url}")
    seconds = 0
    if reminder is None:
        embed.add_field(name='Warning', value='Please specify what do you want me to remind you about.') # Error message
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        embed.add_field(name='Warning',
                        value='Please specify a proper duration, send `reminder_help` for more information.')
    elif seconds > 7776000:
        embed.add_field(name='Warning', value='You have specified a too long duration!\nMaximum duration is 90 days.')
    else:
        await ctx.send(f"Alright, I will remind you about {reminder} in {counter}.")
        await asyncio.sleep(seconds)
        await ctx.send(f"Hi, you asked me to remind you about {reminder} {counter} ago.")
        return
    await ctx.send(embed=embed)

pm.jsonsave("https://api.exchangerate-api.com/v4/latest/USD", "us.json")

@client.event
async def on_ready():
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="if u type f.help"))
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="FOR THE HOMIES"))
    #await client.change_presence(activity=discord.Streaming(name="Youtube", url='https://www.youtube.com/watch?v=vgJTun6G0C8&list=PLG-hoVYF31dvzMsWyuDLnzXQDKfx4_WpI&index=1'))
    # await client.change_presence(status=discord.Status.idle)
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='The Boys'))
    channel = client.get_channel(804982824490369054)
    await channel.send("running through <https://replit.com/@darelife/Floyd-cogs-1#main.py>")
    print('ight..........lets start')


async def ch_pr():
    await client.wait_until_ready()
    while not client.is_closed():
        hmm = ["a song", f'{len(client.guilds)} servers', "fhelp", "You"]
        #nice = [await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name='a fucking song')), await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name=f'{len(client.guilds)} servers')), await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="f.help")), await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="You", status=discord.Status.dnd))]
        #todo = random.choice(nice)

        #status = discord.Status.dnd
        #game = discord.ActivityType.listening(name = "with the API")
        #await client.change_presence(status=discord.Status.idle, activity=game, afk = False, shard_id = 2)

        status1 = random.choice(hmm)
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=2, name=status1))
        await asyncio.sleep(300)
client.loop.create_task(ch_pr())

#to load the cogs (on_command)
@client.command(hidden=True)
async def load(ctx, extension):
  if ctx.author.id == 497352662451224578 or ctx.author.id == 629243339379834880:
    client.load_extension(f'cogs.{extension}')

#to unload the cogs on command
@client.command(hidden=True)
async def unload(ctx, extension):
  if ctx.author.id == 497352662451224578 or ctx.author.id == 629243339379834880:
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_raw_reaction_add(payload):
        if payload.message_id == 824189310868914178:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

            if payload.emoji.name == ':computer:' :
                role = discord.utils.get(guild.roles, name ='TypingRacePing')
            #else:
                #role = discord.utils.get(guild.roles, name =role)
            if role is not None:
                member = payload.member
                if member is not None:
                    await member.add_roles(role)
                    print('done')
                else:
                    print('member not found')
            else:
                print('role not found')

@client.event
async def on_raw_reaction_remove(payload):
    payload.message_id == 824189310868914178
    guild = client.get_guild(payload.guild_id)

    member = await client.guilds[0].fetch_member(payload.user_id)
        
    if str(payload.emoji.name) == "wow":
        role = discord.utils.get(guild.roles, name = "wow")

        await member.remove_roles(role)
        
with open('afk_users_list.txt', 'r') as h:
    afk_list1 = h.readlines()

@client.command()
async def rand1(a):
    # a = await ctx.send('sup')
    guild = await client.fetch_guild(697493731611508737)
    print(guild.name)
    e = discord.utils.get(guild.emojis, name='sadge')
    await a.message.add_reaction(e)

@client.command()
async def ping(ctx):
    #random text....don't pay attention to it
    await ctx.send(f'Pong! {int(client.latency*1000)} ms (the number might remain stable for a while cuz i have got money to buy a stable server!!!) 3')

sad = ["sad", "depressed", "sadge ", "bad", "boring", "lost", "depressing", "depress", "cry", "cries", "crying", ":(", "hard", "bored"]
# you'll need to edit the reactions and replace them with your own reactions. eg: Non-animated-emoji -> "<:emoji_name:emoji_id>", Animated-emoji -> "<a:emoji_name:emoji_id>"
sadreactions = ["<:pepecries:837507320270815252>", "<:pepecrying:837507321570918400>", "<:pepesad:837508592155754526>", "<:pepesadge:837508114646564914>", "<:depressed:837507320731664414>", "<:owosadness:837507322783727659>"]

@client.event
async def on_message(ctx):
    #just made this one for the ppl who play krunker
    if ctx.content.startswith("https://krunker.io/?game"):
        await ctx.delete()
        linkchar = []
        x = 0
        while x < 34:
            linkchar.append(ctx.content[x])
            x += 1
        link = ''.join([str(element) for element in linkchar])
        embed = discord.Embed(title = "My Krunker Game's Link", description = f"""[`Click Here To Join The Game`]({link})
```Game Id : {link[29:]}```""", timestamp = ctx.created_at, color = random.choice(colour))
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = "https://mir-s3-cdn-cf.behance.net/projects/404/a09146108307929.Y3JvcCwxMzgwLDEwODAsMjcwLDA.png")
        embed.set_footer(text = "Enjoy Your Game")
        text = f"```{ctx.content}```"
        if ctx.content != link:
          await ctx.channel.send(text, embed = embed)
        else:
          await ctx.channel.send(embed = embed)
    #this block is made to work only for the dms my bot receives and i make it send the dm'd text to me in a specific channel
    try:
            a = ctx.channel.name
    except:
            channel = client.get_channel(769789003230216215)
            try:    
                embed = ctx.embeds[0]
                await channel.send(f"""{ctx.content} 
                ~ {ctx.author.name}#{ctx.author.discriminator} aka <@!{ctx.author.id}>""", embed = embed)
            except:
                await channel.send(f"""{ctx.content} 
                ~ {ctx.author.name}#{ctx.author.discriminator} aka <@!{ctx.author.id}>""")
    #this thing adds a random sad reaction to the messageif it contains a word that's in the "sad words" list. The bot will remove the reaction after 20 seconds tho.
    if random.randint(0,10) <= 1:
      if " " in ctx.content:
        for x in sad:
          x = f" {x} "
          if x in ctx.content:
              print(x)
              em = random.choice(sadreactions)
              await ctx.add_reaction(em)
              await asyncio.sleep(20)
              await ctx.remove_reaction(em, client.user)
              break
      else:
        for x in sad:
          if x in ctx.content:
            if x == ctx.content:
              print(x)
              em = random.choice(sadreactions)
              await ctx.add_reaction(em)
              await asyncio.sleep(20)
              await ctx.remove_reaction(em, client.user)
              break
      #so like that's my id and whenever someone pings me, my bot would appear to be typing....i've hashed out the thing tho...like u can un-hash it
    # if '<@!497352662451224578>' in ctx.content:
    #     await ctx.channel.trigger_typing()
    #     await asyncio.sleep(5)
    
    #this thing will like show an embed of the message if you share the message link (it's not completely perfect tho. like i made it to share the dank memer memes and it works properly for it
    if 'https://discord.com' in ctx.content:
      if ctx.author.id != 829870450657198121:
        webhooks = await ctx.channel.webhooks()
        hmm = ctx.content
        hmm = f'nice{hmm}'
        a = list(hmm.split('https://discord.com/channels/'))
        b = a[1]
        c = b.split("/")
        guildid = c[0]
        channelid = int(c[1])
        q = c[2]
        messageid = int(f'{q[0]}{q[1]}{q[2]}{q[3]}{q[4]}{q[5]}{q[6]}{q[7]}{q[8]}{q[9]}{q[10]}{q[11]}{q[12]}{q[13]}{q[14]}{q[15]}{q[16]}{q[17]}')
        msg = await client.get_channel(channelid).fetch_message(messageid)
        try:
            att = (msg.attachments[0])
        except:
            a = 'ifkenk'
        #author = msg.author
        #embed=discord.Embed(description = msg.content, timestamp = msg.created_at)
        try:
            embed2 = discord.Embed(title = "Jump", description = f"[Go To Message!](https://discord.com/channels/{guildid}/{channelid}/{messageid})", timestamp = ctx.created_at)
            embed2.set_footer(text = msg.channel.name)
            text = str(msg.author)
            embed2.set_author(name=text[:-5], icon_url=msg.author.avatar_url)
        except:
            pass
        link123 = f"https://discord.com/channels/{guildid}/{channelid}/{messageid}"
        msgcon = ctx.content.replace(link123, "")
        print(msgcon)
        try:
          if msg.embeds[0].url != 'Embed.Empty':
            embed=discord.Embed(title = msg.embeds[0].title, description = msg.content, timestamp = msg.created_at, url = msg.embeds[0].url)
          elif msg.embeds[0].title != 'Embed.Empty':
            embed=discord.Embed(title = msg.embeds[0].title, description = msg.content, timestamp = msg.created_at)
        except:
            embed=discord.Embed(description = msg.content, timestamp = msg.created_at)
        try:
            embed.set_image(url = msg.embeds[0].image.url)
        except:
            pass
        try:
          if str(msg.embeds[0].description) != 'Embed.Empty':
            embed.add_field(name = 'Embed Description', value = msg.embeds[0].description)
        except:
            pass
        try:
            if str(msg.embeds[0].footer) != 'Embed.Empty':
              embed.set_footer(text = str(msg.embeds[0].footer.text))
        except:
           pass
        try:
            embed.set_image(url = att.url)
        except:
            pass
        try:
          if webhooks[0] != None:
            for webhook in webhooks:
              try:
                await webhook.send(msgcon, username=ctx.author.name, avatar_url=ctx.author.avatar_url, wait=True, embeds = (embed, embed2))
                break
              except: pass
        except:
            await ctx.channel.create_webhook(name = "Fone")
            webhooks = await ctx.channel.webhooks()
            for webhook in webhooks:
                await webhook.send(content = msgcon, username=ctx.author.name, avatar_url=ctx.author.avatar_url, wait=True, embeds = (embed, embed2))
                break
    
    #for the afk command
    if ('<@') in ctx.content:
      try:
        message1 = f' {ctx.content}'
        woah = list(message1.split('<'))
        woah.pop(0)
        noice = ''.join([str(element) for element in woah])
        yes = list(noice.split('>'))  
        fnu4jfn = yes[0]
        noice1 = ''.join([str(element) for element in fnu4jfn])
        a = list(noice1.split('!'))
        a.pop(0)
        hmm = a[0]
        okay = hmm[:-1]
        ye = ''.join([str(element) for element in okay])
        print(ye)
        fh = open('afk_users_list.txt')
        filter_object = filter(lambda a: (ye) in a, fh)

        for line in filter_object:
                    c=list(line)
                    p = ''.join([str(element) for element in c])
                    a = []
                    x = 0
                    for c in p:
                        while x < 18:
                            a.append(p[x])
                            x += 1
                    de = ''.join([str(element) for element in a])
                    use = client.get_user(int(de))
                    await ctx.reply(f'{use.name} is {p[22:]}')
      except:
          pass
        #damn = open('afk_users_list.txt')
        #afk_list = damn.readlines()
        #for i in afk_list:
            #i1 = list(i)
            #woah1 = i1[:-1]
            #woah1 = ''.join([str(element) for element in woah1])
            #if (ye) in woah1:
                #if (ye) in woah1:
                    #await ctx.channel.send('He is AFK rn...Please try later.')
    member = ctx.author.id
    with open('afk_users_list.txt', 'r') as h:
      afk_list = h.readlines()
      for i in afk_list:
        if str(member) in i:
          afk_list.remove(i)
          with open('afk_users_list.txt','w') as s:
            for y in afk_list:
                  if '/n' not in y:
                    y = y + '/n'
            for x in afk_list:
                    s.write(f'{x}\n')
                #s.write(str(afk_list))
            await ctx.reply('Removed you from afk.')
    await client.process_commands(ctx)

keep_alive.keep_alive()
token = os.environ.get("TOKEN")
client.run(token)
