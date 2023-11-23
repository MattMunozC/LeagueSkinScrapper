import requests
from bs4 import BeautifulSoup as bs4
def iteration(function):
    def new_function():
        list=[]
        counter=0
        r=requests.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")
        bs=bs4(r.text,"html.parser")
        championlist=bs.find_all("table")[1].find_all("div",{"class":"floatleft"})
        for i in championlist:
            scrapping=bs4(requests.get("https://leagueoflegends.fandom.com/"+i.a['href']+"/Cosmetics").text,"html.parser")
            main_frame=scrapping.find_all("div",{"class":"mw-parser-output"})[0].find_all("div",{"style":"font-size:small"})[0]
            skins=main_frame.find_all("a",{"class":"image"})
            for j in skins:
                list,counter=function(j,counter,list)
    return new_function
@iteration
def download(j,counter=0,list=None):
    print(j,counter,list)
    with open(f"{counter}.jpg","wb") as download:
        image=requests.get(j['href']).content
        download.write(image)
        download.close()
    counter+=1
    return None,counter
@iteration
def list(j,counter=0,list=None):
    list.append(j['href'].split("/")[-3])
    with open("leagueChamp.js","w") as f:
        f.write(f"export var leaguechamp = {str(list)}")
    return list,None
download()



