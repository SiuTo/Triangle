#! /usr/bin/env python3

from tkinter import *

Width, Height = 300, 300
Radius = 5


class Point:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def dist(self, p):
		return ((self.x-p.x)**2+(self.y-p.y)**2)**0.5
	
	def within(self, x, y, r):
		return abs(self.x-x)<r and abs(self.y-y)<r


class PointLabel(Label):

	def __init__(self, parent, label, p):
		Label.__init__(self, parent, text="{} = ({}, {})".format(label, p.x, p.y), font="Arial", width=15, anchor=W)
		self.label = label
	
	def text(self, p):
		self["text"] = "{} = ({}, {})".format(self.label, p.x, p.y)


class LineLabel(Label):
	
	def __init__(self, parent, label, dist=0.0):
		Label.__init__(self, parent, text="{} = {:.2f}".format(label, dist), font="Arial", width=15, anchor=W)
		self.label = label

	def text(self, dist):
		self["text"] = "{} = {:.2f}".format(self.label, dist)


class DrawingBoard(Canvas):

	def __init__(self, parent, width, height):
		Canvas.__init__(self, parent, width=width, height=height)
		self.select_point = -1
		self.bind("<Button-1>", self.set_point)
		self.bind("<B1-Motion>", self.poll)
		self.bind("<ButtonRelease-1>", self.release_point)
	
	def create_point(self, p):
		return self.create_oval(p.x-Radius, p.y-Radius, p.x+Radius, p.y+Radius, fill="blue", activefill="lightblue")

	def set_point(self, event):
		if p0.within(event.x, event.y, Radius):
			self.select_point = 0
		elif p2.within(event.x, event.y, Radius):
			self.select_point = 2
		else:
			self.select_point = -1

	def poll(self, event):
		if self.select_point==0:
			p0.y = min(max(event.y, Radius), Height-Radius)
			self.coords(pointA, p0.x-Radius, p0.y-Radius, p0.x+Radius, p0.y+Radius)
			self.coords(textA, p0.x-3*Radius, p0.y)
			self.coords(triangle, p0.x, p0.y, p1.x, p1.y, p2.x, p2.y)

			labelA.text(p0)
			lineAB.text(p0.dist(p1))
			lineAB2.text(p0.dist(p1)**2)
			lineAC.text(p0.dist(p2))
			lineAC2.text(p0.dist(p2)**2)
		elif self.select_point==2:
			p2.x = min(max(event.x, Radius), Width-Radius)
			self.coords(pointC, p2.x-Radius, p2.y-Radius, p2.x+Radius, p2.y+Radius)
			self.coords(textC, p2.x, p2.y+3*Radius)
			self.coords(triangle, p0.x, p0.y, p1.x, p1.y, p2.x, p2.y)

			labelC.text(p2)
			lineBC.text(p1.dist(p2))
			lineBC2.text(p1.dist(p2)**2)
			lineAC.text(p0.dist(p2))
			lineAC2.text(p0.dist(p2)**2)

	def release_point(self, event):
		self.select_point = -1


p0 = Point(50, 50)
p1 = Point(50, 250)
p2 = Point(250, 250)

app = Tk(className="Triangle")
app.config(padx=10, pady=10)

board = Frame(app, padx=10, pady=10)
board.pack()
labelA = PointLabel(board, "A", p0)
labelA.grid(row=1, column=1)
labelB = PointLabel(board, "B", p1)
labelB.grid(row=2, column=1)
labelC = PointLabel(board, "C", p2)
labelC.grid(row=3, column=1)

lineAB = LineLabel(board, "AB", p0.dist(p1))
lineAB.grid(row=1, column=2)
lineAB2 = LineLabel(board, "AB^2", p0.dist(p1)**2)
lineAB2.grid(row=1, column=3)

lineBC = LineLabel(board, "BC", p1.dist(p2))
lineBC.grid(row=2, column=2)
lineBC2 = LineLabel(board, "BC^2", p1.dist(p2)**2)
lineBC2.grid(row=2, column=3)

lineAC = LineLabel(board, "AC", p0.dist(p2))
lineAC.grid(row=3, column=2)
lineAC2 = LineLabel(board, "AC^2", p0.dist(p2)**2)
lineAC2.grid(row=3, column=3)

Label(board, text="AB^2 + BC^2 = AC^2", font="Arial").grid(row=4, column=2, pady=10)

draw = DrawingBoard(app, width=Width, height=Height)
draw.pack()

triangle = draw.create_polygon(p0.x, p0.y, p1.x, p1.y, p2.x, p2.y, fill="red")
pointA = draw.create_point(p0)
textA = draw.create_text(p0.x-3*Radius, p0.y, text="A")
pointB = draw.create_point(p1)
textB = draw.create_text(p1.x-3*Radius, p1.y+3*Radius, text="B")
pointC = draw.create_point(p2)
textC = draw.create_text(p2.x, p2.y+3*Radius, text="C")

mainloop()

