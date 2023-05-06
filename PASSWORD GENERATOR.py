import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

a = random.choice(["red","lightblue","green"])
b = random.choice(["black","purple","orange"])

def make_password():
    acxz1 = int(password_entry.get())
    long_o = "AABCÇDEFGĞHIİJKLMNOÖPRSŞTKUÜVYZX"
    short_o = long_o.lower()
    nums = "0123456789"
    symbols = ">|<[](),;.:-_/\\+?#*"

    all = long_o + short_o + nums + symbols
    
    if acxz1 > 30:
        warn = Tk()
        warn.withdraw()
        messagebox.showerror("ERROR","YOU CAN'T ENTER THE MAX VALUE")
        password_info["text"] = "INVALID"
        return 0
    if acxz1 < 0:
        warn2 = Tk()
        warn2.withdraw()
        messagebox.showerror("ERROR","YOU CAN'T MİNUS NUMBER")
        password_info["text"] = "INVALID"
        return 0
    if acxz1 == 0:
        warn2 = Tk()
        warn2.withdraw()
        messagebox.showerror("ERROR","YOU MUST ENTER MİN 1 VALUE")
        password_info["text"] = "INVALID"
        return 0

    for x in range(1):
        password = "".join(random.sample(all, acxz1))
        password_info["text"] = str(password)
        
    
pg = tk.Tk()
pg.title("PASSWORD MANAGER")
pg.geometry("300x150")
pg.minsize(400,150)
pg.maxsize(400,150)
password_info = tk.Label(pg,text = "PLEASE ENTER YOUR PASSWORD LENGHT WHAT YOU WANT\n AND PRESS BUTTON\n(PASSWORD WİLL BE İN THİS HERE)",fg = a,bg = b)
password_info.place(width = 400,height = 50,x = 0,y = 0)
password_info2 = tk.Label(pg,text = "PASSWORD\nLENGHT:\n(MAX:30)",fg = a,bg = b)
password_info2.place(width = 100,height = 50,x = 0,y = 50)
password_entry = tk.Entry(fg = b,bg = a)
password_entry.place(width = 300,height = 50,x = 100,y = 50)
password_button = tk.Button(pg,text = "MAKE PASSWORD",fg = a,bg = b,command = make_password)
password_button.place(width = 400,height = 50,x = 0,y = 100)
pg.mainloop()

