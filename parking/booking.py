import tkinter as tk
from tkinter import *
import mysql.connector as con


li = []

mydb = con.connect(
    host="play.altrexmc.com",
    user="u27_mxYn85fXSj",
    password="fR70.^en+hGRFsqcH7fOYqR4",
    database="s27_python",
    port=3306
)


def handle():
    mydb = con.connect(
        host="play.altrexmc.com",
        user="u27_mxYn85fXSj",
        password="fR70.^en+hGRFsqcH7fOYqR4",
        database="s27_python",
        port=3306
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM parking_system")
    rows = cursor.fetchall()
    for i in rows:
        if (i[1]):
            li.append(i[0])
    mydb.close()



def init():
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS parking_system(i INTEGER PRIMARY KEY, status INTEGER)")
    mycursor.execute("SELECT * FROM parking_system")
    rows = mycursor.fetchall()
    if (len(rows) == 0):
        for i in range(10):
            mycursor.execute(f"INSERT INTO parking_system(i, status) VALUES({i},0)")
            mydb.commit()
            mycursor.close()
    handle()


def insert(i: int):
    li.append(i)
    mycursor = mydb.cursor()
    mycursor.execute(f"UPDATE parking_system SET status = 1 WHERE i = {i}")
    mydb.commit()
    mycursor.close()

def remove(i: int):
    if i in li:
        li.remove(i)
    mycursor = mydb.cursor()
    mycursor.execute(f"UPDATE parking_system SET status = 0 WHERE i = {i}")
    mydb.commit()
    mycursor.close()

def getAll():
    return li

def main():
    init()

    root = tk.Tk()
    root.title = "parking_system"
    root.geometry("400x400")
    buttons = []
    buttons.append(tk.Button(root,text='0', command=lambda: insert(0)))
    buttons.append(tk.Button(root, text='1', command=lambda: insert(1)))
    buttons.append(tk.Button(root, text='2', command=lambda: insert(2)))
    buttons.append(tk.Button(root, text='3', command=lambda: insert(3)))
    buttons.append(tk.Button(root, text='4', command=lambda: insert(4)))
    buttons.append(tk.Button(root, text='5', command=lambda: insert(5)))
    buttons.append(tk.Button(root, text='6', command=lambda: insert(6)))
    buttons.append(tk.Button(root, text='7', command=lambda: insert(7)))
    buttons.append(tk.Button(root, text='8', command=lambda: insert(8)))
    buttons.append(tk.Button(root, text='9', command=lambda: insert(9)))


    row = 0
    column = 0
    Grid.columnconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 1, weight=1)
    Grid.rowconfigure(root, 0, weight=1)
    for i in buttons:
        if column == 2:
            row += 1
            Grid.rowconfigure(root, row, weight=1)
            column = 0
        i.grid(row=row, column=column, sticky='NSEW')
        column += 1
    root.mainloop()
