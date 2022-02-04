import requests
from bs4 import BeautifulSoup
import json
from task1 import scrape_top_list
movies=scrape_top_list()
def group_by_year(movies):
    dic={}
    for i in movies:
        movie_year=[]
        year=i["Year"]
        if year not in dic:
            for j in movies:
                # print(j)
                if j["Year"]==year:
                    movie_year.append(j)
                dic[year]=movie_year
        with open("task2.json","w+") as movie_data:
            json.dump(dic,movie_data,indent=4)
    
    return dic

group_by_year(movies)