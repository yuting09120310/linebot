import json
import os
import random
import re
from urllib import parse, request
# import psycopg2
import requests
from bs4 import BeautifulSoup
import pymysql
import time


db_settings = {
        "host":"us-cdbr-east-06.cleardb.net",
        "db":"heroku_8760c94dd464d66",
        "user":"b51153f5c0e98d",
        "password":"11bb074c",
        "port": 3306,
        "charset": "utf8"
    }

def record(keyword):
    data = keyword.split(' ')

    # 抓當下時間
    t = time.localtime()
    result = time.strftime("%Y-%m-%d", t)

    try:
        
        conn = pymysql.connect(**db_settings)

        cursor = conn.cursor()

        command = "INSERT INTO record (name, high_mmHg, low_mmHg, pulse, time) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(command, (data[0], data[1], data[2] , data[3] , result))
    
        conn.commit()
            
        return "紀錄完成囉"

    except Exception as ex:
        return "紀錄失敗，資料有誤，請重新確認。"


def show(keyword):
    data = keyword.split(' ')
    inFo = ""
    conn = pymysql.connect(**db_settings)

    cursor = conn.cursor()
    command = "SELECT time, high_mmHg, low_mmHg, pulse From record WHERE name = " + "'" + data[1] + "'"
    cursor.execute(command)

    result = cursor.fetchall()
    inFo = "        時間         最高      最低   脈搏" + "\n"
    result = list(result)
    for item in result:
        inFo += ("----------------------------------") + "\n"
        inFo += ("|" +str(item[0]) + "  |  " + str(item[1]) + "   |   " + str(item[2]) + "  | " + str(item[3]) + "|") + "\n"
    
    inFo += ("----------------------------------") + "\n"
    print(inFo)
    return inFo