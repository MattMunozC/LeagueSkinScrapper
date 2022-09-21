#Quick formating for leaguechamp.js file
#Purpose: Better readability of the file
if __name__=="__main__":
    with open("leaguechamp.js","r") as f:
        inf=f.read()
        with open("new_league_champ.js","w") as o:
            for i in inf.split(",")[:-1]:
                i.replace("'",'"')
                o.write(f"{i},\n")
            o.write(f"{i}]")