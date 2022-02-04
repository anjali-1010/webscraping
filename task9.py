import random
import time
import requests
import os
import json
from bs4 import BeautifulSoup
from task1 import scrape_top_list
t1=scrape_top_list()
with open("task1.json","r+") as file:
    a=json.load(file)
def  txt():
    random_sleep=random.randint(1,3)
    for i in a:
        path="/home/admin123/Desktop/task9/task9"+i["Movie_Name"]+".json"
        if os.path.exists(path):
            pass
        else:
            create=open("/home/admin123/Desktop/task9/task9"+i["Movie_Name"]+".json","w")
            url=requests.get(i["url"])
            create1=create.write(url.text)
            create.close()
        time.sleep(random_sleep)
txt()

