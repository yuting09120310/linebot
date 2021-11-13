import os

from bs4 import BeautifulSoup
from urllib import request
import requests
import random
import psycopg2
import json

def ticketInfo(keyword):
    data = keyword.split(' ')

    inFo = ""
    resp = requests.get('https://www.ptt.cc/bbs/MobileComm/index.html')
    soup = BeautifulSoup(resp.text, 'html.parser')
    main_titles = soup.find_all('div', 'title')

    

    if(len(data) > 1):
        for title in main_titles:
            if data[1] in title.text:
                inFo += title.text.strip() + "\n"
                inFo += "https://www.ptt.cc" + title.find("a")['href'] + "\n"
    else:
        for title in main_titles:
            if "本文已被刪除" in title.text:
                pass
            else:
                inFo += title.text.strip() + "\n"
                inFo += "https://www.ptt.cc" + title.find("a")['href'] + "\n"

    print(inFo)
    return inFo
    
# def test():
#     str = "ptt 3c iphone12" 
#     data = str.split(' ')
#     print(len(data))
# test()

ticketInfo("ptt")