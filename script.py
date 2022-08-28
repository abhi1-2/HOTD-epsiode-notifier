import requests
from bs4 import BeautifulSoup
import os
import time
 


m4uhd_link = "https://m4uhd.cc/watch-tvseries-house-of-the-dragon-2022--269399.html"
episode_no = 2

while(True):
    x = requests.get(m4uhd_link).text
    html = BeautifulSoup(x, 'html.parser')

    episode_count = 0
    for b in html.find_all('button'):
        if(b.get('class')[0]=='episode'):
            episode_count+=1

    if(episode_count)> (episode_no - 1):
        os.system("say 'New Episode'")
        print("New Episode")
        # break
    else:
        time.sleep(10)
        
        # os.system("say 'No New Episode'")
    
