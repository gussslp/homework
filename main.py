import tkinter as tk
import requests
import json
from tkinter import *
from tkinter import messagebox

window = tk.Tk()
window.title("app")
window.minsize(width=300, height=300)
window.maxsize(width=500, height=500)

ah = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method"
def userdata():
    global json_get
    get_url = ah+"=getdata&user="+str(entry1.get())
    res2 = requests.get(get_url)
    json_get = res2.json()

def yep():
    userdata()
    if json_get[0]['id'] == None:
        messagebox.showerror("Error",message="No such id exist")
    else:
        url = ah+"=setbalance&user="+str(entry1.get())+"&balance="+str(entry2.get())
        res = requests.get(url)
        json = res.json()
        userdata()
        print("ПІБ: "+json_get[0]['name']+" "+json_get[0]['surname']+" "+"Пошта: "+json_get[0]['email']+" "+"Група: "+json_get[0]['school_group']+" "+"Баланс: "+json_get[0]['balance'])

entry1 = tk.Entry()
entry1.pack()

entry2 = tk.Entry()
entry2.pack()

button = tk.Button(text="Змінити баланс",bg="white",fg="green",command=yep)
button.pack()

window.mainloop()
#