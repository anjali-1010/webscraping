import json
from task1 import scrape_top_list
from task4 import movie_details

all_movie=scrape_top_list()
top_movies=all_movie[:100]
def get_movie_details_list():
    list1=[]
    for i in top_movies:
        k=i["url"]
        list1.append(movie_details(k))

    with open("task5.json","w") as file5:
        json.dump(list1,file5,indent = 4)
    file5.close()
    return list1
get_movie_details_list()
