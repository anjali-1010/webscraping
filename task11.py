import json 
from bs4 import BeautifulSoup

with open("task5.json") as file:
    genre=json.load(file)
def movies_genre(genre):
    dict={}
    for i in genre:
        if "Genre" in i:
            genre=i["Genre"]
            # print(genre)
            for j in genre:
                # print(j)
                if j not in dict:
                    # genre=i["Genre"]
                    dict[j]=1
                else:
                    dict[j]+=1
            else:
                continue
        print(dict)
        with open("task11.json","w+")as file6:
            json.dump(dict,file6,indent=4)

movies_genre(genre)

