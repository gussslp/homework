import sqlite3
import sqlite3 
import tkinter as tk
from tkinter import *

db = sqlite3.connect("sqlite.db")

c = db.cursor()

#c.execute(""" CREATE TABLE users(
#entry,
#entry1
#)""")
window = tk.Tk()
window.title("My app")
window.minsize(width=300, height=300)
window.maxsize(width=500, height=500)

def text():
    tex = (entry.get())
    tex1 = (entry1.get())
    c.execute("INSERT INTO users VALUES ('%s','%s')"%(tex,tex1))
    db.commit()
    c.execute("SELECT rowid FROM users")
    a = max(c.fetchall())
    c.execute("SELECT * FROM users")
    d = a[0]
    b = c.fetchall()
    text.insert(tk.END,b[d-1])

label = tk.Label(text="Hello world", bg="white", fg="red")
label.pack()
entry = tk.Entry()
entry.pack()

label1 = tk.Label(text="Hello world", bg="white", fg="red")
label1.pack()
entry1 = tk.Entry()
entry1.pack()

button = tk.Button(text="Button",bg="white", fg="green", command=text)
button.pack()

text = tk.Text(width=30, height=30)
scrollbar = Scrollbar(orient=VERTICAL,command=text.yview)
scrollbar.pack(side="right",fill="y")
text.configure(yscrollcommand=scrollbar.set)
text.pack()

window.mainloop()
db.close()