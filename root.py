# -*- coding: utf-8 -*-
import tkinter as tk
import sys
import numpy
import os
sys.path.append(os.path.join(sys.path[0], '../../../Documents/Projects/LaserScan/Blocks/'))
import Face


root=tk.Tk()
root.title("Lazario  alfa 0.1.0") #Название окна
root.configure(bg='#313440')
root.geometry('900x700') #Разрешение окна
root.resizable(False, False) #запрет маштабирования


Win = Face.Blocks(root)

canvas = tk.Canvas(root, width=900, height=300, bg='#313440')
canvas.place(x=0,y=300)

for y in range(12):
    k = 78 * y
    canvas.create_line(20+k, 277, 20+k, 20, width=2, fill= '#666')

for x in range(9):
    k = 32 * x
    canvas.create_line(20, 20+k, 877, 20+k, width=2, fill= '#666')

root.mainloop()
