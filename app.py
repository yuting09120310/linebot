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
from objFun import stock, ticketInfo, Product
from MRT import Taipei_MRT
from healthy import record, show
#======這裡是呼叫的檔案內容=====

#======python的函數庫===========
import tempfile, os
import datetime
import time
#======python的函數庫===========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('8BZ9LzUQ2K+wNey55D2YBizL0uzn8z7KIm6wTce/ZZH049XdAPwcvOFRN6I677edwlRETPsMjojgC1nar412H4RDJudNNyOiNu/ep9zDqk7UTKMwiG1+dTwJuiMe1LH+0agJt2iSp1U8ZtcgfU3SvAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('427b391391ee1f542cb3a46526462d52')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    user_keyword = msg.lower()
    str_keyword = user_keyword.split(' ')[0]

    outInfo = ''

    if '最新合作廠商' in user_keyword:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif '阿公' in str_keyword:
        outInfo += record(user_keyword)
        message = TextSendMessage(text=outInfo)
        line_bot_api.reply_message(event.reply_token,message)
    elif '阿嬤' in str_keyword:
        outInfo += record(user_keyword)
        message = TextSendMessage(text=outInfo)
        line_bot_api.reply_message(event.reply_token,message)
    elif '查詢' in str_keyword:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '查找' in str_keyword:
        outInfo += show(user_keyword)
        message = TextSendMessage(text=outInfo)
        line_bot_api.reply_message(event.reply_token,message)
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
