import os

from bs4 import BeautifulSoup
from urllib import request
import requests
import random
import psycopg2
import json
import re

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
    
def dcard():
    inFo = ""
    headers = {
        'user-agent': 'Mozilla/5.0'
    }
    resp = requests.get('https://www.dcard.tw/f/pet', headers = headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    main_titles = soup.find_all('a',href=re.compile(r'pet/p/'))
    for data in main_titles:
        inFo += data.text + "\n"
        url = "https://www.dcard.tw" + data.get('href')
        inFo += url + "\n"
    print(inFo)
    return inFo