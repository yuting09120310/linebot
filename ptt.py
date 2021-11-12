from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import requests
from bs4 import BeautifulSoup
def function_ptt():
    message = TextSendMessage(
        text="是否註冊成為會員？",
    #     res = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
    #     soup = BeautifulSoup(res.text,"html.parser")
    #     for item in soup.select('.r-ent'):
    #         message = item.select('.title')[0].text
    )
    return message 

