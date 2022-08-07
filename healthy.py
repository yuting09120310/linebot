import json
import os
import random
import re
from urllib import parse, request
# import psycopg2
import requests
from bs4 import BeautifulSoup
import pymysql

def record(keyword):

    db_settings = {
        "host":"us-cdbr-east-06.cleardb.net",          # 主機名稱
        "db":"heroku_8760c94dd464d66", # 資料庫名稱
        "user":"b51153f5c0e98d",        # 帳號
        "password":"11bb074c",   # 密碼
        "port": 3306,
        "charset": "utf8"
    }

    try:
        conn = pymysql.connect(**db_settings)

        cursor = conn.cursor()
        command = "INSERT INTO record (name, high_mmHg, low_mmHg, pulse, time) VALUES (%s,%s,%s,%s,%s)"
        # 取得華語單曲日榜
        cursor.execute(command, ("alex", "100", "63" , "56" , "2022-08-08"))
                
            # 儲存變更
        conn.commit()
            

        print("連線成功")

    except Exception as ex:
        print(ex)



data = input()
record(data)