import discord
from discord.ext import commands
import random
import json

snipe_message_content = []
snipe_message_sender = []
snipe_message_channel = []
snipe_message_sender_pfp = []
s_1_content = []
s_1_sender = []
s_1_channel = []

colour = [0xDC143C, 0xD35400, 0x48C9B0, 0x7FB3D5, 0xffa0a2]

def write_json(data, filename='data.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 

class snipe(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('snipe.py is running')

    @commands.Cog.listener()
    async def on_message_delete(self, message):
    #     with open('data.json') as json_file: 
    #             data = json.load(json_file) 
    #             temp = data['Messages'] 
  
    # # python object to be appended 
    #             y = {"content":message.content, 
    #                  "Author's ID": message.author.id, 
    #                  "Author's name": message.author.name,
    #                  "Server" : message.guild.name,
    #                  "Channel" : message.channel.name,
    #                  "Message ID" : message.id,
    #                  "Channel ID" : message.channel.id,
    #                  "Guild ID" : message.guild.id,
    #                  "Link" : f'https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}'
    #                 }
    #             temp.append(y)       
    #     write_json(data)  
    #     snipe_message_content.append(message.content)
    #     snipe_message_sender.append(message.author.display_name)
    #     snipe_message_channel.append(message.channel.name)
    #     s_1_content.append(message.content)
    #     s_1_sender.append(message.author.display_name)
    #     s_1_channel.append(message.channel.name)
    try:
                warnsfile = open(f"{message.guild.name}.txt", "a+")
                warnsfile.write(f'{message.author.display_name} said ```{message.content}``` in {message.channel}. The User Also Sent {message.attachments[0].url}\n')
    except:
                warnsfile = open(f"{message.guild.name}.txt", "a+")
                hour_ist = int(str(message.created_at)[10:-13])
                hour_ist += 5
                min_ist = int(str(message.created_at)[14:-10])
                min_ist += 30
                if min_ist >= 60:
                    hour_ist += 1
                    min_ist -= 60
                if hour_ist >= 24:
                    hour_ist -= 24
                sec_ist = int(str(message.created_at)[17:-7])
                if len(str(min_ist)) == 1:
                    min_ist = f"0{min_ist}"
                if len(str(hour_ist)) == 1:
                    min_ist = f"0{hour_ist}"
                if len(str(sec_ist)) == 1:
                    min_ist = f"0{sec_ist}"
                warnsfile.write(f'{message.author.display_name} said ```{message.content}``` in {message.channel} - {str(message.created_at)[:10]} {hour_ist}:{min_ist}:{sec_ist}\n')

    @commands.command(aliases=['s'])
    async def snipe(self, ctx, number: int = 1):
        "credits : Maximilian and xNoir"
        c_random_int = random.randint(0, len(colour)-1)
        if number < 10:
                x = -1
                embed = discord.Embed(title = 'Snipe', color = colour[c_random_int])
                while x+1 < number:
                    x = x+1
                    #ight_channel = str(snipe_message_channel[x])
                    #ight_sender = str(snipe_message_sender[x])
                    #ight_content = str(snipe_message_content[x])
                    #await ctx.channel.send(f"{ight_sender} said {ight_content} in {ight_channel}")
                    fh = open(f'{ctx.guild.name}.txt')
                    ooh = fh.readlines()
                    ooh.reverse()
                    oof = ooh[x]
                    for line in ooh:
                        p = ''.join([str(element) for element in oof])
                    embed.add_field(name = 'Message', value = p, inline=False)
                await ctx.channel.send(embed = embed)
        else:
                await ctx.channel.send('Sorry, but could you please keep the number below 10?')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
      warnsfile = open(f"reactions{payload.guild_id}.txt", "a+")
      if payload.emoji.id != None:
        warnsfile.write(f'<@!{str(payload.user_id)}> reacted with <:{str(payload.emoji.name)}:{payload.emoji.id}> https://discord.com/channels/{payload.guild_id}/{payload.channel_id}/{payload.message_id}\n')
      elif payload.emoji.id == None:
        warnsfile.write(f'<@!{str(payload.user_id)}> reacted with {str(payload.emoji.name)} https://discord.com/channels/{payload.guild_id}/{payload.channel_id}/{payload.message_id}\n')

    @commands.command(aliases=['r_snipe', 'rs'])
    async def reactionsnipe(self, ctx, number: int = 1):
        if number < 10:
            if number != 1:
                x = -1
                reactionnumber = 1
                embed = discord.Embed(title = ' Reaction Snipe')
                while x+1 < number:
                    x = x+1
                    fh = open(f'reactions{ctx.guild.id}.txt')
                    ooh = fh.readlines()
                    ooh.reverse()
                    oof = ooh[x]
                    for line in ooh:
                        p = ''.join([str(element) for element in oof])
                        linklist =  list(p.split(" "))
                        link = linklist[-1]
                    embed.add_field(name = f'Reaction {reactionnumber}', value = f"""{p[:-86]} 
[`Link To The Message`]({link})""", inline=False)
                    reactionnumber += 1
                await ctx.channel.send(embed = embed)

            elif number == 1:
                    fh = open(f'reactions{ctx.guild.id}.txt')
                    ooh = fh.readlines()
                    ooh.reverse()
                    oof = ooh[0]
                    for line in ooh:
                        p = ''.join([str(element) for element in oof])
                        linklist =  list(p.split(" "))
                        link = linklist[-1]
                    embed = discord.Embed(title = "Reaction Snipe", description = f"""{p[:-86]} 
[Link To The Message]({link})""")
                    await ctx.channel.send(embed = embed)

        else:
            await ctx.reply("Can you please enter a number smaller than 10")
                
def setup(client):
    client.add_cog(snipe(client))
