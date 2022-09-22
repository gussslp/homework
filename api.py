import requests
import json
import tkinter as tk
from tkinter import *


window = tk.Tk()
window.title("app")
window.minsize(width=300, height=300)
window.maxsize(width=500, height=500)

def ch():
	url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"
	querystring = {"country":entry.get().capitalize()}
	headers = {
		"X-RapidAPI-Key": "f84c35f3femshb10e79c767c5081p19081bjsnae44ca5eec8f",
		"X-RapidAPI-Host": "covid-19-coronavirus-statistics.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	json1 = json.loads(response.text)

	label2['text'] = "CheckTime"+str(json1["data"]["lastChecked"])+"\n"+"country: "+str(json1["data"]["location"])+"\n"+"deaths: "+str(json1["data"]["deaths"])

label =tk.Label(text="coronavirus checker", fg="black")
label.pack()

label1 =tk.Label(text="\n enter country", fg="green")
label1.pack()

entry = tk.Entry()
entry.pack()

Button = tk.Button(text="Check", command=ch)
Button.pack()

label2 =tk.Label(text="", fg="red")
label2.pack()



window.mainloop()
