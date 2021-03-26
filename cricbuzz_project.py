#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


baseurl='https://www.cricbuzz.com'
url='https://www.cricbuzz.com/cricket-team'
r=requests.get(url)
soup=BeautifulSoup(r.content,'lxml')


# In[3]:


page=soup.find_all('div',class_='cb-col cb-col-100')
team_link=[]
for link1 in page:
    for link2 in link1.find_all('a',href=True):
            team_link.append(baseurl+link2['href']+'/players')
team = [] 
for links in team_link: 
    if links not in team: 
        team.append(links)  


# In[4]:


players=[]
for teams in team:
    req=requests.get(teams)
    soupie=BeautifulSoup(req.content,'lxml')
    names=soupie.find_all('div',class_='cb-col-67 cb-col cb-left cb-top-zero')
    
    for i in names:
        for j in i.find_all('a',href=True):
            players.append(baseurl + j['href'])
players


# In[20]:


len(players)


# In[110]:


play=['https://www.cricbuzz.com/profiles/1413/virat-kohli',
 'https://www.cricbuzz.com/profiles/576/rohit-sharma',
 'https://www.cricbuzz.com/profiles/1446/shikhar-dhawan']


# In[135]:


import urllib3
import re
cat=[]
info=[]
names=[]

for i in players:
    http = urllib3.PoolManager()
    r = http.request('get',i )
    
    

    main_data = r.data
    main_data = str(main_data)
    name = re.search('class="cb-font-40">(.*?)<',str(main_data))
    name = name.group(1)
    #find the unique tags for whole container 
    main_data1 = main_data.split('cb-col-40')
    
    for i in main_data1:
        a = re.search('>(.*?)<.*?">(.*?)<', str(i))
        if a:
            #print(a.group(1), a.group(2))
            cat1 = a.group(1)
            info1 = a.group(2)
            if cat1!='Teams':
                
                cat.append(cat1)
                info.append(info1)
                names.append(name)
            else:
                continue

        else :
            cat1=''
            info1=''
            continue


# In[136]:


dictionary = {'name':names,'info':cat, 'details':info }


# In[137]:


import pandas as pd
df=pd.DataFrame(dictionary)
df


# In[138]:


import numpy as np
df=df.replace('',np.nan)


# In[139]:


df.dropna(inplace=True)


# In[140]:


df.reset_index(drop=True,inplace=True)


# In[142]:


df1=df.set_index(['name','info','details'])
df1.head(20)


# In[147]:


df1.shape


# In[149]:


df1


# In[ ]:




