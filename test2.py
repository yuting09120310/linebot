from datetime import date, datetime

now_h = datetime.now().strftime('%H:%M')

if(now_h > '00:11'):
    print(now_h)
else:
    print('0911')
