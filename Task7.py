import json 
from bs4 import BeautifulSoup

# from task5 import get_movie_details_list

with open("task5.json") as file:
    director=json.load(file)

    # director=get_movie_details_list()
def analyse_movies_directors(director):
    dict={}
    for i in director:
        # print(i)
        dir_name=i["Director"]
        # print(dir_name)
        for j in dir_name:
            if j  not in dict:
                dir_name=j
                dict[j]=1
            else:
                dict[j]+=1
        print(dict)
    with open("task7.json","w+")as file7:
        json.dump(dict,file7,indent=4)
analyse_movies_directors(director)