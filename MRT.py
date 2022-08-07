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
            
        if(key[1] in data[0]['StationName']['Zh_tw']):
            # print("去程")
            info = '當前為去程 班表如下 \n' + timetable(data[0]['StationName']['Zh_tw'],0)
            return info
        else:
            # print("回程")
            info = '當前為回程 班表如下 \n' + timetable(data[1]['StationName']['Zh_tw'],1)
            return info
    else:
        print('輸入錯誤')


def timetable(startStation,Direction):
    info=[]
    info2=""
    day = datetime.today().isoweekday()
    now_time = datetime.now().strftime('%H:%M')

    # Direction 營運路線方向描述 : [0:'去程',1:'返程']
    base = "https://ptx.transportdata.tw/MOTC/v2/Rail/Metro/StationTimeTable/TRTC?$filter="
    url = f"StationName/Zh_tw eq '{startStation}' and Direction eq '{Direction}' and ServiceDay/ServiceTag eq '平日' &$top=30&$format=JSON"

    if(day > 5):
        url = f"StationName/Zh_tw eq '{startStation}' and Direction eq '{Direction}' and ServiceDay/ServiceTag eq '假日' &$top=30&$format=JSON"

    response = request('get', base+url, headers= a.get_auth_header())
    content = response.content.decode()  #重新編碼 預設空的為utf8
    data = json.loads(content)

    print(base+url)

    for i in range(0,len(data)):
        timetables = data[i]['Timetables']
        for j in range (0,len(timetables)):
            if(now_time <= timetables[j]['ArrivalTime']):
                info.append(timetables[j]['ArrivalTime'])

    info = list(set(info))
    info.sort()

    for k in range(0,3):
        info2 += info[k] + '\n'

    return info2