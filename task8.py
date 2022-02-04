import requests
import os
import json 
from bs4 import BeautifulSoup
from task1 import scrape_top_list
t1=scrape_top_list()
with open("task1.json","r+") as file:
    a=json.load(file)
def  txt():
    for i in a:
        path=("/home/admin123/Desktop/task8/task8"+i["Movie_Name"]+".text")
        if os.path.exists(path):
            pass
        else:
            create=open("/home/admin123/Desktop/task8/task8"+i["Movie_Name"]+".text","w")
            url=requests.get(i["url"])
            create1=create.write(url.text)
            create.close()
txt()


















# a=[[2,3,4],[6,2,9],[7,4,3]]
# i=0
# m=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# print(max)
    