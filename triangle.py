#! /usr/bin/env python3

from tkinter import *

Width, Height = 300, 300
Radius = 5
x0, y0, x1, y1, x2, y2 = 50, 50, 50, 250, 250, 250
selete_point = -1

def dist(x1, y1, x2, y2):
	return ((x1-x2)**2+(y1-y2)**2)**0.5

def create_point(canvas, x, y):
	return canvas.create_oval(x-Radius, y-Radius, x+Radius, y+Radius, fill="blue", activefill="lightblue")

def set_point(event):
	global selete_point
	if abs(event.x-x0)<Radius and abs(event.y-y0)<Radius:
		selete_point = 0
	elif abs(event.x-x2)<Radius and abs(event.y-y2)<Radius:
		selete_point = 2
	else:
		select_point = -1

def poll(event):
	global selete_point, x0, y0, x1, y1, x2, y2
	if selete_point==0:
		y0 = min(max(event.y, Radius), Height-Radius)
		draw.coords(pointA, x0-Radius, y0-Radius, x0+Radius, y0+Radius)
		draw.coords(textA, x0-3*Radius, y0)
		draw.coords(triangle, x0, y0, x1, y1, x2, y2)

		labelA["text"] = "A = ({}, {})".format(x0, y0)
		lineAB["text"] = "AB = {:.2f}".format(dist(x0, y0, x1, y1))
		lineAB2["text"] = "AB^2 = {:.2f}".format(dist(x0, y0, x1, y1)**2)
		lineAC["text"] = "AC = {:.2f}".format(dist(x0, y0, x2, y2))
		lineAC2["text"] = "AC^2 = {:.2f}".format(dist(x0, y0, x2, y2)**2)
	elif selete_point==2:
		x2 = min(max(event.x, Radius), Width-Radius)
		draw.coords(pointC, x2-Radius, y2-Radius, x2+Radius, y2+Radius)
		draw.coords(textC, x2, y2+3*Radius)
		draw.coords(triangle, x0, y0, x1, y1, x2, y2)

		labelC["text"] = "C = ({}, {})".format(x2, y2)
		lineBC["text"] = "BC = {:.2f}".format(dist(x1, y1, x2, y2))
		lineBC2["text"] = "BC^2 = {:.2f}".format(dist(x1, y1, x2, y2)**2)
		lineAC["text"] = "AC = {:.2f}".format(dist(x0, y0, x2, y2))
		lineAC2["text"] = "AC^2 = {:.2f}".format(dist(x0, y0, x2, y2)**2)

def release_point(event):
	global selete_point
	selete_point = -1

app = Tk(className="Triangle")
app.config(padx=10, pady=10)

board = Frame(app, padx=10, pady=10)
board.pack()
labelA = Label(board, text="A = ({}, {})".format(x0, y0), font="Arial", width=15, anchor=W)
labelA.grid(row=1, column=1)
labelB = Label(board, text="B = ({}, {})".format(x1, y1), font="Arial", width=15, anchor=W)
labelB.grid(row=2, column=1)
labelC = Label(board, text="C = ({}, {})".format(x2, y2), font="Arial", width=15, anchor=W)
labelC.grid(row=3, column=1)

lineAB = Label(board, text="AB = {:.2f}".format(dist(x0, y0, x1, y1)), font="Arial", width=15, anchor=W)
lineAB.grid(row=1, column=2)
lineAB2 = Label(board, text="AB^2 = {:.2f}".format(dist(x0, y0, x1, y1)**2), font="Arial", width=15, anchor=W)
lineAB2.grid(row=1, column=3)

lineBC = Label(board, text="BC = {:.2f}".format(dist(x1, y1, x2, y2)), font="Arial", width=15, anchor=W)
lineBC.grid(row=2, column=2)
lineBC2 = Label(board, text="BC^2 = {:.2f}".format(dist(x1, y1, x2, y2)**2), font="Arial", width=15, anchor=W)
lineBC2.grid(row=2, column=3)

lineAC = Label(board, text="AC = {:.2f}".format(dist(x0, y0, x2, y2)), font="Arial", width=15, anchor=W)
lineAC.grid(row=3, column=2)
lineAC2 = Label(board, text="AC^2 = {:.2f}".format(dist(x0, y0, x2, y2)**2), font="Arial", width=15, anchor=W)
lineAC2.grid(row=3, column=3)

Label(board, text="AB^2 + BC^2 = AC^2", font="Arial").grid(row=4, column=2, pady=10)

draw = Canvas(app, width=Width, height=Height)
draw.pack()

triangle = draw.create_polygon(x0, y0, x1, y1, x2, y2, fill="red")
pointA = create_point(draw, x0, y0)
textA = draw.create_text(x0-3*Radius, y0, text="A")
pointB = create_point(draw, x1, y1)
textB = draw.create_text(x1-3*Radius, y1+3*Radius, text="B")
pointC = create_point(draw, x2, y2)
textC = draw.create_text(x2, y2+3*Radius, text="C")
draw.bind("<Button-1>", set_point)
draw.bind("<B1-Motion>", poll)
draw.bind("<ButtonRelease-1>", release_point)

mainloop()
