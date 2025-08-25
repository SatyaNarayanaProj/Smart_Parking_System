from tkinter import *
import tkinter as tk

def handle():
    f = open("data.txt", "w")
    f.write("")
    f.close()

def insert(i: int):
    f = open("data.txt", "r")
    line = f.readline()
    li = []
    iterator = list(line.rsplit(" "))
    for j in iterator:
        li.append(str(j))
    li.append(str(i))
    f.close()
    f = open("data.txt", "w")
    f.write(str(" ".join(li)))
    f.close()


def remove(i: int):
    f = open("data.txt", "r")
    line = f.readline()
    li = []
    iterator = list(line.rsplit(" "))
    for j in iterator:
        li.append(str(j))
    try:
        li.remove(str(i))
    except ValueError:
        pass
    print(li)
    f.close()
    f = open("data.txt", "w")
    st = str(" ".join(li))
    f.write(st)
    f.close()

def getAll():
    f = open("data.txt", "r")
    line = f.readline()
    li = []
    iterator = list(line.rsplit(" "))
    for j in iterator:
        li.append(str(j))
    f.close()
    return li

def main():
    handle()

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