import json
data=open("task5.json","r+")
a=json.load(data)
d=a[:48] #49,50,51
def analyse_director(movie_list):
    directors_dic={}
    for movie in movie_list:
        for director in movie["Director"]:
            directors_dic[director]={}
    for i in range(len(movie_list)):
        for director in directors_dic:
            
            if director in movie_list[i]["Director"]:
                language=movie_list[i]["Language"]
                directors_dic[director][language]=0
    for i in range(len(movie_list)):
        for director in directors_dic:
            if director in movie_list[i]["Director"]:
                language=movie_list[i]["Language"]
                directors_dic[director][language]+=1
    with open("task10.json","w+") as file:
                json.dump(directors_dic,file,indent=4)
                return directors_dic
analyse_director(d)
# import json
# data=open("task5.json","r+")
# a=json.load(data)
# d=a[52:]
# def analyse_director_language(movie_list):
#     directors_dic={}
#     for movie in movie_list:
#         for director in movie["Director"]:
#             directors_dic[director]={}
#     for i in range(len(movie_list)):
#         for director in directors_dic:
#             if director in movie_list[i]["Director"]:
#                 language=movie_list[i]["Language"]
#                 directors_dic[director][language]=0
#     for i in range(len(movie_list)):
#         for director in directors_dic:
#             if director in movie_list[i]["Director"]:
#                 language=movie_list[i]["Language"]
#                 directors_dic[director][language]+=1
#     with open("Task10.json","w+") as file:
#                 json.dump(directors_dic,file,indent=4)
#                 return directors_dic
# analyse_director_language(d)