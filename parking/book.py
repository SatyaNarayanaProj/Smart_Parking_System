import tkinter as tk
from parking import data

root = tk.Tk()
tk.Button(root,text='0', command=lambda: data.insert(0)).pack()
tk.Button(root, text='1', command=lambda: data.insert(1)).pack()
tk.Button(root, text='2', command=lambda: data.insert(2)).pack()
tk.Button(root, text='3', command=lambda: data.insert(3)).pack()
tk.Button(root, text='4', command=lambda: data.insert(4)).pack()
tk.Button(root, text='5', command=lambda: data.insert(5)).pack()
tk.Button(root, text='6', command=lambda: data.insert(6)).pack()
tk.Button(root, text='7', command=lambda: data.insert(7)).pack()
tk.Button(root, text='8', command=lambda: data.insert(8)).pack()
tk.Button(root, text='9', command=lambda: data.insert(9)).pack()
root.mainloop()
