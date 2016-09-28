import tkinter as tk
import matplotlib.pyplot as plt

root= tk.Tk()
root.title("Polynomial Graph Plotter")

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

def Plotter():
	P=list(map(int,entry.get().split(',')))
	x= list(int(llimit.get())),int(ulimit.get())),0.5)
	



entry = tk.Entry(root, width=40, fg='black' ,bg='white')
llimit= tk.Entry(root, width=10, fg='black', bg='white')
ulimit= tk.Entry(root, width=10, fg='black', bg='white')
plot_button = tk.Button(root,text=b,width=5,relief=rel,command=Plotter,fg='white',bg='black')

root.mainloop()
