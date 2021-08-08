import discord
from discord.ext import commands
from discord.utils import get

class dontghostpingus(commands.Cog):
    
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('"Dont ghost ping me" is running')
    
    #So this one is basically like if someone pings you and then deletes the ping (aka a ghost ping), the bot will dm you will details like :-
    #the author of the message - his/her id, nickname in the server, 
    #channel name, server name
    #the link of the deletd message...it won't show the message but it will give you the idea of the location of the message in the chats (like it will show the messages sent before and after it)
    #and obviously the content of the message
    @commands.Cog.listener()
    async def on_message_delete(self, message):
      if ('<@!your_discord_id>') in str(message.content):
          user = self.client.get_user("your_discord_id")
          if user.id != message.author.id:
             #Before you go through all of this, remember that sometimes ghost pings might be an accident and the author of the message might not intend to do it.
             #you can un-hash the text below this if you want to notify the author of the message like in the channel...but it might get annoying for everyone sometimes
             #await message.channel.send(f'||<@!{message.author.id}>|| aka {message.author} why do u want to ghost ping my boss?')
             embed=discord.Embed(title='Ping', description=(f'''||<@!{message.author.id}>|| aka {message.author.display_name} pinged you in {message.channel} in the {message.guild} server'''))
             embed.add_field(name='LINK', value=(f'https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}'))
             embed.add_field(name='message', value=f'{message.content}')
             #you can also add the time at which the message was created using "message.created_at" 
             await user.send(embed=embed)

def setup(client):
    client.add_cog(dontghostpingus(client))
