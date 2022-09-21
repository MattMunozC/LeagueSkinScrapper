import requests
from bs4 import BeautifulSoup as bs4
def download():
    counter=0
    r=requests.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")
    bs=bs4(r.text,"html.parser")
    championlist=bs.find_all("table")[1].find_all("div",{"class":"floatleft"})
    for i in championlist:
        scrapping=bs4(requests.get("https://leagueoflegends.fandom.com/"+i.a['href']+"/Cosmetics").text,"html.parser")
        main_frame=scrapping.find_all("div",{"class":"mw-parser-output"})[0].find_all("div",{"style":"font-size:small"})[0]
        skins=main_frame.find_all("a",{"class":"image"})
        for j in skins:
            download=open(str(counter)+".jpg","wb")
            image=requests.get(j['href']).content
            download.write(image)
            download.close()
            counter+=1
def list():
    list=[]
    r=requests.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")
    bs=bs4(r.text,"html.parser")
    championlist=bs.find_all("table")[1].find_all("div",{"class":"floatleft"})
    for i in championlist:
        scrapping=bs4(requests.get("https://leagueoflegends.fandom.com/"+i.a['href']+"/Cosmetics").text,"html.parser")
        main_frame=scrapping.find_all("div",{"class":"mw-parser-output"})[0].find_all("div",{"style":"font-size:small"})[0]
        skins=main_frame.find_all("a",{"class":"image"})
        for j in skins:
            list.append(j['href'].split("/")[-3])
    output=open("leagueskin.txt","w").write(str(list))
    output.close()
if __name__=="__main__":
    list()



