import json 
from bs4 import BeautifulSoup

# from task5 import get_movie_details_list

# language=get_movie_details_list()
with open("task5.json") as file:
    language=json.load(file)
def analyse_movies_language(Language):
    dict={}
    for i in language:
        if "Language" in i:
            Language=i["Language"]
            if Language not in dict:
                Language=i["Language"]
                dict[Language]=1
            else:
                dict[Language]+=1
        else:
            continue
    print(dict)
    with open("task6.json","w+")as file6:
        json.dump(dict,file6,indent=4)
analyse_movies_language(language)