# -*- coding: utf-8 -*-
import tkinter as tk
import sys
import numpy
import os
sys.path.append(os.path.join(sys.path[0], '../../../Документы/Projects/LaserScan/Blocks/'))
import Face

root=tk.Tk()
root.title("Lazario  alfa 0.1.0") #Название окна
root.configure(bg='#313440')
root.geometry('900x700') #Разрешение окна
root.resizable(False, False) #запрет маштабирования


Win = Face.Blocks(root)

root.mainloop()
