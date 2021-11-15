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

def stock(keyword):
    inFo = ""
    data = keyword.split(' ')
    headers = {
        'user-agent': 'Mozilla/5.0'
    }
    resp = requests.get('https://tw.stock.yahoo.com/quote/' + data[1] + '.TW', headers = headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    main_titles = soup.find_all('h2',re.compile(r'Fz'))
    inFo += main_titles[0].text + '\n'
    main_titles = soup.find_all('span',re.compile(r'Fz'))
    inFo += main_titles[1].text + '\n'
    inFo += main_titles[2].text + '\n'
    inFo += main_titles[9].text + '\n'

    print(inFo)
    return inFo
    
#代理問題
# def dcard():
#     inFo = ""
#     headers = {
#         'user-agent': 'Mozilla/5.0'
#     }
#     proxy = {
#     'http': '18.179.120.38:80'
#     }
#     resp = requests.get('https://www.dcard.tw/f/pet', headers = headers, proxies = proxy)
#     soup = BeautifulSoup(resp.text, 'html.parser')
#     main_titles = soup.find_all('a',href=re.compile(r'pet/p/'))
#     for data in main_titles:
#         inFo += data.text + "\n"
#         url = "https://www.dcard.tw" + data.get('href')
#         inFo += url + "\n"
#     print(inFo)
#     return inFo

#以下字典
# def dec():
#     inFo = ""
#     headers = {
#         'user-agent': 'Mozilla/5.0'
#     }
#     resp = requests.get('https://blog.amazingtalker.com/zh-tw/zh-eng/%E5%9C%8B%E9%AB%98%E4%B8%AD%E5%BF%85%E8%83%8C8000%E5%96%AE%E5%AD%97%E8%A1%A8/3747/', headers = headers)
#     soup = BeautifulSoup(resp.text, 'html.parser')
#     main_titles = soup.find_all('td',re.compile(r'tg-yw4l'))
#     path = 'output.txt'
#     f = open(path, 'w' ,encoding="utf-8")

#     for item in main_titles:
#         f.write(item.text + '\n')
#     f.close()

    
    