from django.contrib import admin
from .models import UserData
import requests
import json
import sqlite3


url = 'https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=clients'
res = requests.get(url)
json = res.json()
stolb = ["id", "full_name","email","address","phone_number","current_balance", "last_payment", "reg_date", "lastcall_date", "status"]
db = sqlite3.connect('db.sqlite3')
c = db.cursor() 

for num in range(0,1350):
    a = [json[num]["id"],json[num]["full_name"],json[num]["email"],json[num]["address"],json[num]["phone_number"],json[num]["current_balance"],json[num]["last_payment"],json[num]["reg_date"],json[num]["lastcall_date"],json[num]["status"]]
    c.execute('INSERT INTO myapp_userdata VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9]))
db.commit()
db.close()


admin.site.register(UserData)