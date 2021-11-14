from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
from ptt import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time




def handle_message(user_keyword):
    # msg = event.message.text
    # user_keyword = msg.lower()
    outInfo = ''
    if '最新合作廠商' in user_keyword:
        print(user_keyword)
    # elif '最新活動訊息' in msg:
    #     message = buttons_message()
    #     line_bot_api.reply_message(event.reply_token, message)
    # elif '註冊會員' in msg:
    #     message = Confirm_Template()
    #     line_bot_api.reply_message(event.reply_token, message)
    # elif '旋轉木馬' in msg:
    #     message = Carousel_Template()
    #     line_bot_api.reply_message(event.reply_token, message)
    # elif '圖片畫廊' in msg:
    #     message = test()
    #     line_bot_api.reply_message(event.reply_token, message)
    # elif '功能列表' in msg:
    #     message = function_list()
    #     line_bot_api.reply_message(event.reply_token, message)
    elif 'ptt' in user_keyword:
        outInfo += ticketInfo(user_keyword)
        print(outInfo)
    elif 'dcard' in user_keyword:
        outInfo += test()
        print(outInfo) 
    else:
        print(outInfo) 

handle_message("最新合作廠商")