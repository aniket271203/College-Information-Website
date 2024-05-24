#!/bin/python3
import matplotlib.pyplot as plt
import sqlite3
import requests
# from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
class DBclass:
    def __init__(self, path):
        self.path = path
        self.db = sqlite3.connect(self.path)
        self.cur = self.db.cursor()

    def execute(self, query):
        self.cur.execute(query)
        return [i[0] for i in self.cur.description], self.cur.fetchall()
headers = {"Accept-Language": "en-US, en;q=0.5"}
url="https://www.iiit.ac.in/people/faculty/"
results = requests.get(url, headers=headers)
movie_soup = BeautifulSoup(results.text, "html.parser")
movie_div = movie_soup.find_all('tr')
for container in movie_div:
        image_url=container.find_all('td')[0].find_all('div',class_='image-wrapper')[0].find_all('img')[0]['src']
        url="https://www.iiit.ac.in"+image_url
        name = container.find_all('td')[1].h3.a.text
        name2=[]
        for ch in name:
                if ch=='[':
                      break
                else:
                      name2.append(ch)
        
        email= ('').join(name2).strip().replace(".","").replace("  ","").replace("   ","").replace("    ","").replace(" ",".").lower()
        email2=email+"@iiit.ac.in"
        # print(email2)
        data2=container.find_all('p')[0].text.strip().replace('*\n','').replace('\n','').split('    ')
        position=data2[0].strip()
        education_college=data2[-1].strip()
        data3=container.find_all('p')[1].text.strip().replace('*\n','').replace('\n','').split(':')
        research_area=(" ").join(data3[1:]).strip()
        data4=container.find_all('p')[2].a.text
        research_lab=data4
        conn = sqlite3.connect('iiit.db')
        c = conn.cursor()
        c.execute('SELECT * FROM faculty WHERE name = ? AND research_lab=? AND research_area=? AND education=?', (name,research_lab,research_area,education_college))
        if c.fetchone() is None:
                c.execute('INSERT INTO faculty (name, position, education, research_area, research_lab, email,image_url) VALUES (?, ?, ?, ?, ?, ?, ?)', (name,position,education_college,research_area,research_lab,email2,url))
        conn.commit()
        conn.close()
        
db = DBclass('iiit.db')
datawhole=db.execute('SELECT * FROM faculty')
print(datawhole)
        # f.write(name+"\n")
        # year = container.h3.find('span', class_='lister-item-year').text
        # f.write(year+"\n")
        # runtime = container.p.find('span', class_='runtime').text if container.p.find('span', class_='runtime').text else '-'
        # f.write(runtime+"\n")
        # imdb = container.find('div',class_='lister-item-content').find('div',class_='ipl-rating-widget').find('div',class_='ipl-rating-star small').find('span',class_='ipl-rating-star__rating').text
        # f.write(imdb+"\n")
        # nv = container.find_all('span', attrs={'name': 'nv'})
        # grosses = nv[1].text if len(nv) > 1 else '-'
        # f.write(grosses+"*")
        # grosses=container.find('div',class_='list-description').p.b.text
        # f.write(grosses+"\n")
        # geners=container.p.find('span',class_='genre').text.replace("\n","")
        # f.write(geners+"\n")
# f.close()
# f=open("q1txt.txt","r")
# content=f.read()
# cont_list=content.split("\n")
# dic={}
# list_gross=[]
# list_name=[]
# for i in range(1000):
#     if i<100:
#         list_name.append(cont_list[i*6]+" "+cont_list[i*6+1])
#         list_gross.append(int(cont_list[i*6+4].replace("$","").replace(",","")))
#     genre_list=cont_list[i*6+5].replace(",","").split()
#     for genres in genre_list:
#         if genres in dic:
#             dic[genres]+=1
#         else:
#             dic[genres]=1
        

# genre = list(dic.keys())
# gen_freq = list(dic.values())
# fig = plt.figure(figsize = (80, 5))
# plt.xlabel("frequency of genre")
# plt.ylabel("genre")
# plt.title("Genre vs frequency bar graph")
# plt.barh(genre, gen_freq, color ='red')
# plt.savefig("graph1.png")
# plt.figure(figsize=(30,30))
# plt.plot(list_name, list_gross, '-')
# plt.xticks(rotation = -90 , fontsize=10)
# plt.savefig("graph2.png")
# f.close()


