import tkinter as tk
import matplotlib.pyplot as plt
import math



def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

def F(x,P):
		for t in x:
			n=0
			s=0
			for i in P:
				s+=i*math.pow(t,n)
				n+=1
			yield s

def Plotter():
	P= list(map(float,entry.get().split(',')))
	x= list(frange(int(llimit.get()),int(ulimit.get()),0.5))
	y= list(F(x,P))
	plt.plot(x,y)
	plt.show()
	

root= tk.Tk()
root.title("Polynomial Graph Plotter")
root.geometry("300x100")

entry = tk.Entry(root, width=40, fg='black' ,bg='white')
llimit= tk.Entry(root, width=10, fg='black', bg='white')
ulimit= tk.Entry(root, width=10, fg='black', bg='white')
plot_button = tk.Button(root,text="Plot",width=5,command=Plotter,fg='white',bg='black')

entry.pack()
llimit.pack()
ulimit.pack()
plot_button.pack()



root.mainloop()
