import requests
from bs4 import BeautifulSoup as bs4
from pprint import pprint
OUTPUT_DIRECTORY="Results"
def iteration(function):
    def new_function():
        list=[]
        counter=0
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }
        r=requests.get("https://leagueoflegends.fandom.com/wiki/List_of_champions",headers=headers)
        bs=bs4(r.text,"html.parser")
        championlist=bs.find_all("table",{"class","article-table"})[0].find_all("tr")[1::]
        for i in championlist:
            url=requests.get("https://leagueoflegends.fandom.com/"+i.a['href']+"/Cosmetics",headers=headers)
            scrapping=bs4(url.text,"html.parser")
            main_frame=scrapping.find_all("div",{"class":"mw-parser-output"})[0].find_all("div",{"style":"font-size:small"})[0]
            skins=main_frame.find_all("a",{"class":"image"})
            for j in skins:
                name=j['href'].split("/")[-3]
                print(name)
                list,counter=function(j,counter,list,name,format="count")
    return new_function
@iteration
def download(j,counter=0,list=None,name="",format=None):
    if format=="count": name=f"{counter}.jpg"
    with open(f"{OUTPUT_DIRECTORY}/{name}","wb") as download:
        image=requests.get(j['href']).content
        download.write(image)
        download.close()
    counter+=1
    return None,counter
@iteration
def list(j,counter=0,list=None,name="",format=None):
    list.append(name)
    with open(f"{OUTPUT_DIRECTORY}/leagueChamp.js","w") as f:
        f.write(f"export var leaguechamp = {str(list)}")
    return list,None
download()



