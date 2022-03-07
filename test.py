from hashlib import sha1
import hmac
from wsgiref.handlers import format_date_time
from datetime import date, datetime
from time import mktime
import base64
from requests import request
import json

app_id = '1a05ff6ce5734d2aacac7e0969a53ade'
app_key = 'Gpt_U47acZpGT1HAojFgO1q6Hgw'



class Auth():

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        xdate = format_date_time(mktime(datetime.now().timetuple()))
        hashed = hmac.new(self.app_key.encode('utf8'), ('x-date: ' + xdate).encode('utf8'), sha1)
        signature = base64.b64encode(hashed.digest()).decode()

        authorization = 'hmac username="' + self.app_id + '", ' + \
                        'algorithm="hmac-sha1", ' + \
                        'headers="x-date", ' + \
                        'signature="' + signature + '"'
        return {
            'Authorization': authorization,
            'x-date': format_date_time(mktime(datetime.now().timetuple())),
            'Accept - Encoding': 'gzip'
        }


a = Auth(app_id, app_key)

def Taipei_MRT(key):
    key = key.split(' ')

    if(len(key) == 3):
        base = 'https://ptx.transportdata.tw/MOTC/v2/Rail/Metro/Station/TRTC?$filter='
        url = f"StationName/Zh_tw eq '{key[1]}' or StationName%2FZh_tw eq '{key[2]}'&$top=30&$format=JSON"
        if '/' in url:
            url = url.replace('/', f'%2F')

        if ' ' in url:
            url = url.replace(' ', f'%20')

        response = request('get', base+url, headers= a.get_auth_header())
        content = response.content.decode()  #重新編碼 預設空的為utf8
        data = json.loads(content)

        # print(data)
            
        if(key[1] in data[0]['StationName']['Zh_tw']):
            print("去程")
            info = timetable(data[0]['StationName']['Zh_tw'],0)
            return info
        else:
            print("回程")
            info = timetable(data[1]['StationName']['Zh_tw'],1)
            return info
    else:
        print('輸入錯誤')


def timetable(startStation,Direction):
    info=""
    day = datetime.today().isoweekday()
    now_H = datetime.now().strftime("%H")
    now_M = datetime.now().strftime("%M")

    # Direction 營運路線方向描述 : [0:'去程',1:'返程']
    base = "https://ptx.transportdata.tw/MOTC/v2/Rail/Metro/StationTimeTable/TRTC?$filter="
    url = f"StationName/Zh_tw eq '{startStation}' and Direction eq {Direction} and ServiceDay/ServiceTag eq '平日' &$top=30&$format=JSON"

    if(day > 5):
        url = f"StationName/Zh_tw eq '{startStation}' and Direction eq {Direction} and ServiceDay/ServiceTag eq '假日' &$top=30&$format=JSON"

    response = request('get', base+url, headers= a.get_auth_header())
    content = response.content.decode()  #重新編碼 預設空的為utf8
    data = json.loads(content)

    for i in range(0,len(data)):
        timetables = list(data[i]['Timetables'])
        for item in timetables:
            if((item['ArrivalTime'][0:2] in now_H) & (item['ArrivalTime'][3:6] >= now_M)):
                info += item['ArrivalTime'] + '\n'
    return info
            
key = input()
Taipei_MRT(key)