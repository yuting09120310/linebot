import os

from bs4 import BeautifulSoup
from urllib import request
import requests
import random
import psycopg2
import json

def ticketInfo(keyword):
    inFo = ""
    resp = requests.get('https://www.ptt.cc/bbs/MobileComm/index.html')
    soup = BeautifulSoup(resp.text, 'html.parser')
    main_titles = soup.find_all('div', 'title')

    for title in main_titles:

        if keyword in title.text:
            inFo += title.text.strip() + "\n"
            inFo += "https://www.ptt.cc" + title.find("a")['href'] + "\n"

    return inFo
    
# def test():
#     str = "helloworld"
#     data = str.split(' ')
#     print(data[0])

# test()