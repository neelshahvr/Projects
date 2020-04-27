
import tkinter as tk
from PIL import Image, ImageTk


height_ = 700
width_ = 600



root = tk.Tk()

canvas = tk.Canvas(root, height = height_, width = width_, bg = "#560808")
canvas.pack()

background_image = tk.PhotoImage(file = 'title_scrn.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg = '#000000')
frame.place(relx = .3775, rely = .68, relwidth = .245, relheight = .1)

button1 = tk.Button(frame, text = "Play", bg = "#ffffff")
button1.pack(side = "left", fill = "y")

button2 = tk.Button(frame, text = "Pause", bg = "#ffffff")
button2.pack(side = "left", fill = "y")

button3 = tk.Button(frame, text = "Restart", bg = "#ffffff")
button3.pack(side = "right", fill = "y")

root.mainloop()
