import requests
from bs4 import BeautifulSoup
import json

url=("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")
# print(soup)
def scrape_top_list():
    list=[]
    main_div=soup.find("div",class_="panel-body content_body allow-overflow")
    table=main_div.find("table",class_="table")
    tr=table.find_all("tr")
    for i in tr:
        # print(i)
        dict={}
        td=i.find_all("td")
        for j in td:
            
            
            rank=i.find("td",class_="bold").get_text()[:3]
            dict["Rank"]=rank
            rating=i.find("span",class_="tMeterScore").get_text()[-3:]
            dict["Rating"]=rating
            Movie_Name=i.find("a",class_="unstyled articleLink")["href"][3:]
            dict["Movie_Name"]=Movie_Name
            Number_of_review=i.find("td",class_="right hidden-xs").get_text()
            dict["Number_of_review"]=Number_of_review
            year=i.find("a",class_="unstyled articleLink").get_text()[-5:-1]
            dict["Year"]=year
            # print(dict)

            url=i.find("a",class_="unstyled articleLink")["href"]
            url1="https://www.rottentomatoes.com"+url
            dict["url"]=url1

        list.append(dict)
        if {} in list:
            list.remove({})
    with open("task1.json","w+") as file:
        json.dump(list,file,indent=4)
    return list
movie_data=scrape_top_list()

            
            

          
