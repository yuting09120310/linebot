import requests
from bs4 import BeautifulSoup

def function_ptt():
    res = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
    soup = BeautifulSoup(res.text)
    for item in soup.select('.r-ent'):
        message = item.select('.title')[0].text
    return message
    