#Warning - Check whether your country's laws allow you to scrape data from the internet and also some websites don't allow webscraping and will ban your ip if you do it
#If you try to scrape data from a website too often even if they allow scraping, they will be forced to atleast temporarily banning your ip becuz of the extra traffic generated. 
import discord
from discord.ext import commands
import  requests
from bs4 import BeautifulSoup
import random

def final_name(subject):
    chem = ['c', "chem", "chemistry"]
    phy = ['p', "phy", "physics"]
    math = ['m', "math", "maths", "mathematics"]
    if subject in chem:
        return "Chemistry"
    if subject in math:
        return "Mathematics"
    if subject in phy:
        return "Physics"


colour = [0xDC143C, 0xD35400, 0x48C9B0, 0x7FB3D5, 0xffa0a2]

class search(commands.Cog):
    
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('urban.py is running')

    @commands.command()
    #idk whether they have an api or not....i just made it by scraping data from their website mainly cuz i was learning web scraping.
    async def urban(self, ctx, *, word):
      try:
        hmm = word
        c_random_int = random.randint(0, len(colour)-1)
        hmm.replace(' ', '\%20')
        urban_dictionary = requests.get(f'https://www.urbandictionary.com/define.php?term={hmm}')
        soup = BeautifulSoup(urban_dictionary.content, features="html.parser")
        meaning = (soup.find("div",attrs={"class":"meaning"}).text)
        example = (soup.find("div",attrs={"class":"example"}).text)
        embed=discord.Embed(title=(hmm), description=(meaning), timestamp = ctx.message.created_at, color = colour[c_random_int])
        embed.add_field(name='Example', value=example, inline=False)
        embed.add_field(name='Link', value=f'https://www.urbandictionary.com/define.php?term={hmm}', inline=False)
        embed.set_author(name="Urban Dictionary", url=(f'https://www.urbandictionary.com/define.php?term={hmm}'), icon_url="https://i.pinimg.com/originals/f2/aa/37/f2aa3712516cfd0cf6f215301d87a7c2.jpg")
        await ctx.reply(embed=embed)
      except:
        await ctx.reply('Couldnt find the word on the Urban dictionary')
        
    @commands.command()
    async def covid19(self, ctx, country):
        covid19_link = requests.get(f'https://www.worldometers.info/coronavirus/country/{country}/')
        soup = BeautifulSoup(covid19_link.content, features="html.parser")
        cases = (soup.find("div",attrs={"class":"maincounter-number"}).text)
        ct= soup.findAll("div", {"class" : "maincounter-number"})
        cte= ct[1]
        recovery = ct[2]
        recoveries = recovery.text
        deaths = (cte.text)
        embed=discord.Embed(title=(f'Covid 19 cases in {country}'), description=(cases))
        embed.add_field(name='Number Of Deaths', value=(deaths))
        embed.add_field(name='Number Of Recoveries', value=(recoveries))
        embed.add_field(name="For more info, visit", value=(f'https://www.worldometers.info/coronavirus/country/{country}/'), inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def covid19world(self, ctx):
        covid19_link = requests.get('https://www.worldometers.info/coronavirus/')
        soup = BeautifulSoup(covid19_link.content, features="html.parser")
        cases = (soup.find("div",attrs={"class":"maincounter-number"}).text)
        ct= soup.findAll("div", {"class" : "maincounter-number"})
        cte= ct[1]
        recovery = ct[2]
        recoveries = recovery.text
        deaths = (cte.text)
        embed=discord.Embed(title=('Covid 19 cases in the world'), description=(cases))
        embed.add_field(name='Number Of Deaths', value=(deaths))
        embed.add_field(name='Number Of Recoveries', value=(recoveries))
        await ctx.channel.send(embed=embed)
        
    @commands.command()
    #an ncert command, only for class 11 tho...too lazy to make it for other classes
    #if your school isn't affiliated by the Central Board of Secondary Education (CBSE), ncert books are the books published by the it in india and you don't need to worry about it
    async def ncert(self, ctx, subject, chapter):
      if subject == "rr":
        embed = discord.Embed(title = "NCERT", description = f"""[PDF](https://bit.ly/3g0Mn27)
[Ncert's Website](https://bit.ly/3g0Mn27)
[Download The Book](https://bit.ly/3g0Mn27)""", url = "https://ncert.nic.in/textbook.php", color = discord.Colour.random())
        embed.set_footer(text = f"Chapter : {chapter} | Subject : physics")
        await ctx.send(embed = embed)
      else:
        subname = final_name(subject)
        if len(chapter) == 1:
            chapter1 = f"0{chapter}"
        if subject == 'math' or subject == 'mathematics' or subject == 'm':
            ye = 'm'
            booknumber = '1'
            total = "16"
        elif subject == 'chem' or subject == 'chemistry' or subject == 'c':
            ye = 'c'
            booknumber = '1'
            total = "7"
        elif subject == 'phy' or subject == 'physics' or subject == 'p':
            ye = 'p'
            booknumber = '1'
            total = "8"
        elif subject == 'chem2' or subject == 'chemistry2' or subject == 'c2':
            ye = 'c'
            booknumber = '2'
            total = "7"
        elif subject == 'phy2' or subject == 'physics2' or subject == 'p2':
            ye = 'p'
            booknumber = '2'
            total = "7"
        else:
            embed=discord.Embed(title='Invalid Subject', description = '''```m or math or mathematics -> math
    c or chem or chemistry -> chem
    p or phy or physics -> phy
    c2 or chem2 or chemistry -> chem book 2
    p2 or physics2 or chemistry2 -> physics book 2 ```''')
            await ctx.channel.send(embed=embed)
        if subject in ['m', 'math', 'mathematics', 'chem', 'c', 'chemistry', 'p', 'phy', 'physics', 'c2', 'chem2', 'chemistry2', 'p2', 'phy2', 'physics2']:
            download_link = f"https://ncert.nic.in/textbook/pdf/ke{ye}h{booknumber}dd.zip"
            #creates the embed
            embed = discord.Embed(title = "NCERT", description = f"""[PDF](https://ncert.nic.in/textbook/pdf/ke{ye}h{booknumber}{(chapter1)}.pdf)
[Ncert's Website](https://ncert.nic.in/textbook.php?ke{ye}h{booknumber}={(chapter)}-{total})
[Download The Book]({download_link})""", url = "https://ncert.nic.in/textbook.php", color = discord.Colour.random())
            embed.set_footer(text = f"Chapter : {chapter} | Subject : {subname}")
            await ctx.send(embed = embed)

    @commands.command()
    #It might not work...i am too lazy to find the exact solution but yeah..u can check it out if you want to understand how webscraping works...it's really basic tho...like all my webscraping things are kinda basic
    async def mc(self, ctx, craft):
        url = "https://www.minecraftcrafting.info/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        sup = craft.capitalize()
        sup = f"Craft {sup}"
        images = soup.find_all("img", attrs = {"alt":sup})
        text = "Try making it plural or maybe you entered a non craftable item"
        if len(images) == 0:
            await ctx.send(text)
        for image in images:
            image_src = image["src"]
            print(image)
            url_final = url + image_src
            text = url_final
            await ctx.reply(text)
            if image == None:
                await ctx.reply("Try making it plural or maybe you entered a non craftable item")


def setup(client):
    client.add_cog(search(client))
