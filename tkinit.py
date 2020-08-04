import tkinter as tk
from tkinter import ttk
import db.db
import mysql.connector
from cur import cur

cnx = mysql.connector.connect(user='root', password='Chirag@123', host='localhost',database = 'flaskdb',auth_plugin='mysql_native_password')
cur = cnx.cursor()

def database(tuple):

    cur.execute('select * from python WHERE email = %s',tuple)
    return cur.fetchall()

win = tk.Tk()
win.title('Welcome to Login page')

label1 = ttk.Label(win, text = 'Email-id').grid(row= 0 ,column=0,sticky = tk.W)
label2 = ttk.Label(win, text ='Password').grid(row =1,column =0, sticky = tk.W)

var1 = tk.StringVar()
var2 = tk.StringVar()

entry1 =ttk.Entry(win,textvariable = var1).grid(row =0,column = 1)
entry2 = ttk.Entry(win,textvariable = var2).grid(row =1, column = 1)

def fn():
    email = var1.get()
    password = var2.get()
    if email=="":
        print('Please enter email to login')
    elif password =="":
        print("Please enter password")
    else:
        result = db.db.
        if result:
            print('Login Successfully')
        else:
            print('ERROR')



button = ttk.Button(win,text = 'Login',command = fn).grid(row =2 , column =0)

tk.mainloop()