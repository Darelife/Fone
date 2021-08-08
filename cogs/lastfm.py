#you need to replace the values of person1, person2, person3, etc with your lastfm usernames
#you need to replace the values of person1_discord_id, person2_discord_id, person3_discord_id, etc with your discord id's
from urllib.request import urlopen
import discord
from discord.ext import commands
import requests
import os
import json
import random
 
API_KEY = os.environ['lastfmapikey']
 
colour = [0xDC143C, 0xD35400, 0x48C9B0, 0x7FB3D5, 0xffa0a2]
 
def lastfm_get(payload):
   # define headers and URL
   headers = {'user-agent': USER_AGENT}
   url = 'https://ws.audioscrobbler.com/2.0/'
 
   # Add API key and format to the payload
   payload['api_key'] = API_KEY
   payload['format'] = 'json'
 
   response = requests.get(url, headers=headers, params=payload)
   return response
 
def get_user_artist_plays(sartist, lu):
   link = f"http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&user={lu}&artist={sartist}&api_key={API_KEY}&format=json"
   link = link.replace(" ", "+")
   with urlopen(link) as f:
       data = json.load(f)
   return(data["artist"]["stats"]["userplaycount"])
 
def get_user_album_plays(sartist, salbum, lu):
   link = f"http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={API_KEY}&user={lu}&artist={sartist}&album={salbum}&format=json"
   link = link.replace(" ", "+")
   with urlopen(link) as f:
       data = json.load(f)
   return(data["album"]["userplaycount"])
def get_user_track_plays(sartist, sname, lu):
     link = f"http://ws.audioscrobbler.com/2.0/?method=track.getInfo&user={lu}&api_key={API_KEY}&artist={sartist}&track={sname}&format=json"
     link = link.replace(" ", "+")
     with urlopen(link) as f:
       data = json.load(f)
     return(data["track"]["userplaycount"])
 
def sort_dict_by_value(d, reverse = False):
 return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
 
def who_knows(sartist):
   person1 = int(get_user_artist_plays(sartist, "person1"))
   person2 = int(get_user_artist_plays(sartist, "person2"))
   person5 = int(get_user_artist_plays(sartist, "person5"))
   person4 = int(get_user_artist_plays(sartist, "person4"))
   person3 = int(get_user_artist_plays(sartist, "person3"))
 
   pog2020 = [int(person1), int(person2), int(person5), int(person4), int(person3)]
   x = max(pog2020)
   pog = []
   pog.append(x)
   if x == person1:
       pog.append("person1")
   if x == person2:
       pog.append("person2")
   if x == person5:
       pog.append("person5")
   if x == person4:
       pog.append("person4")
   if x == person3:
       pog.append("person3")
   return(pog)

def recent_tracks_user(lu):
         if lu == "person1":    
             person1_recent = lastfm_get({
            'user' : 'person1',
            'method' : 'user.getRecentTracks'
             })
             jsave(person1_recent.json(),"person1_recenttracks.json")
             file = "person1_recenttracks.json"
             return file
         elif lu == "person5":
             person5_recent = lastfm_get({
            'user' : 'person5',
            'method' : 'user.getRecentTracks'
             })
             jsave(person5_recent.json(),"person5_recenttracks.json")
             file = "person5_recenttracks.json"
             return file
         elif lu == "person4":
             person4_recent = lastfm_get({
                 'user' : 'person4',
                 'method' : 'user.getRecentTracks'
             })
             jsave(person4_recent.json(),"person4_recenttracks.json")
             file = "person4_recenttracks.json"
             return file
         elif lu == "person3":
             person3_recent = lastfm_get({
                 'user' : 'person3',
                 'method' : 'user.getRecentTracks'
             })
             jsave(person3_recent.json(),"person3_recenttracks.json")
             file = "person3_recenttracks.json"
             return file
         elif lu == "person2":
             person2_recent = lastfm_get({
                 'user' : 'person2',
                 'method' : 'user.getRecentTracks'
             })
             jsave(person2_recent.json(),"person2_recenttracks.json")
             file = "person2_recenttracks.json"
             return file
         else:
             return None
 
def artistpic(sartist, salbum):
     link = f"http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={API_KEY}&artist={sartist}&album={salbum}&format=json"
     link = link.replace(" ", "+")
     with urlopen(link) as f:
         #ainfo is the artist info
         ainfo = json.load(f)
     pic = ainfo["album"]["image"][-1]["#text"]
     return pic
    
def genresearch(sartist, sname):
     link = f"http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={API_KEY}&artist={sartist}&track={sname}&format=json"
     link = link.replace(" ", "+")
     with urlopen(link) as f:
         genresss = json.load(f)
     genres = []
     for x in genresss["track"]["toptags"]["tag"]:
         genres.append(x["name"])
     genre = ' - '.join([str(elem) for elem in genres])
     if len(genres) == 0:
         return None
     else:
         return genre
 
users = {
   "person1_discord_id":"person1",
   "person4_discord_id":"person4",
   "person2_discord_id":"person2",
   "person3_discord_id":"person3",
   "person5_discord_id":"person5"}
 
ids = {
   "person1":"person1_discord_id",
   "person4":"person4_discord_id",
   "person2":"person2_discord_id",
   "person3":"person3_discord_id",
   "person5":"person5_discord_id"}
 
USER_AGENT = 'Dataquest'
 
headers = {
   'user-agent': USER_AGENT
}
 
payload = {
   'api_key': API_KEY,
   'method': 'chart.gettopartists',
   'format': 'json'
}
 
r = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
# print(f"initial status code -> {r.status_code}")
 
person1_recent = lastfm_get({
   'user' : 'person1',
   'method' : 'user.getRecentTracks'
})
person2_recent = lastfm_get({
   'user' : 'person2',
   'method' : 'user.getRecentTracks'
})
person3_recent = lastfm_get({
   'user' : 'person3',
   'method' : 'user.getRecentTracks'
})
person4_recent = lastfm_get({
   'user' : 'person4',
   'method' : 'user.getRecentTracks'
})
person5_recent = lastfm_get({
   'user' : 'person5',
   'method' : 'user.getRecentTracks'
})
# print(f"method : 'chart.gettopartists' -> {r.status_code}")
def jsave(obj, file):
   # create a formatted string of the Python JSON object
   text = json.dumps(obj, sort_keys=True, indent=4)
   with open(file, "w") as f:
       f.write(text)
 
jsave(person1_recent.json(),"person1_recenttracks.json")
jsave(person2_recent.json(),"person2_recenttracks.json")
jsave(person3_recent.json(),"person3_recenttracks.json")
jsave(person4_recent.json(),"person4_recenttracks.json")
jsave(person5_recent.json(),"person5_recenttracks.json")
 
 
def jprint(obj):
   # create a formatted string of the Python JSON object
   text = json.dumps(obj, sort_keys=True, indent=4)
   print(text)
 
# jprint(r.json()['artists']['@attr'])
 
class Lastfm(commands.Cog):
  
   def __init__(self, client):
       self.client = client
 
 
   @commands.Cog.listener()
   async def on_ready(self):
       print('lastfm.py is running')
  
   @commands.command()
   #now playing
   async def np(self, ctx):
         #lu is the lastfm username of the author of the message
         lu = users[str(ctx.author.id)]
        
         if recent_tracks_user(lu) != None:
             file = recent_tracks_user(lu)
         elif recent_tracks_user(lu) == None:
             await ctx.send("you aren't registered in my database")
             file = "null"
        
         #extracting data from the file
         if file == "null":
           pass
         else:
             with open(file, "r") as f:
                 data = json.load(f)
            
             if ctx.author.nick == None:
               title = f"{ctx.author.name}'s Last Song"
             else:
               title = f"{ctx.author.nick}'s Last Song"
             jd = data["recenttracks"]["track"][0]
             try:
               if jd["@attr"]["nowplaying"] == "true":
                 if ctx.author.nick == None:
                   title = f"{ctx.author.name}'s Current Song"
                 else:
                   title = f"{ctx.author.nick}'s Current Song"
             except: pass
             sname = jd["name"]
             #the line below is really important
             salbum = jd["album"]["#text"]
             sartist = jd["artist"]["#text"]
             smbid = jd["mbid"]
             almbid = jd["album"]["mbid"]
             armbid = jd["artist"]["mbid"]
             #embed
             np = discord.Embed(title = sname, url = f"https://www.last.fm/user/{lu}", description = f"**{sartist}** | {salbum}", color = random.choice(colour))
             np.set_author(name = title, url = f"https://www.last.fm/user/{lu}", icon_url = ctx.author.avatar_url)
             thumbnail = jd["image"][-1]["#text"]
             np.set_thumbnail(url = thumbnail)
             footer_text = []
             try:
               if genresearch(sartist, sname) != None:
                   footer_text.append(f"• {genresearch(sartist, sname)}")
             except: pass
             a = who_knows(sartist)
             print(a)
             #di is the short for discord id
             b = []
             for x in a:
                 if type(x) != int:
                     di = int(ids[x])
                     user = self.client.get_user(di)
                     b.append(f"{user.display_name}#{user.discriminator}")
             print(b)
             number = a[0]
             a = []
             a.append(number)
             for x in b:
                 a.append(x)
             if len(a) > 2:
                 number = a[0]
                 a.pop(0)
                 await ctx.send(a)
                 wk = '&'.join([str(elem) for elem in a])
                 wk = f"👑{number} ({wk})"
             elif len(a) == 2:
                 wk = f"👑{a[0]} ({a[1]})"
             # try:
             footer_text.append(f"• {get_user_artist_plays(sartist, lu)} artist plays • {get_user_album_plays(sartist, salbum, lu)} album plays • {get_user_track_plays(sartist, sname, lu)} song plays • {wk}")
             # except: pass
             try:
                 footer_text = '\n'.join([str(elem) for elem in footer_text])
                 if footer_text != None:
                       np.set_footer(icon_url = artistpic(sartist, salbum), text = footer_text)
                 else:
                       np.set_footer(icon_url = artistpic(sartist, salbum), text = "Powered by lastfm")
             except: pass
             await ctx.send(embed = np)
            
 
 
def setup(client):
   client.add_cog(Lastfm(client))


