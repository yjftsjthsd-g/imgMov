#!/usr/bin/env python3

from tkinter import *
from sys import argv
from PIL import Image

class App:
	def __init__(self, master, photo, destA, destB):
		frame = Frame(master)
		frame.pack()
		self.f = frame

		self.destA = destA
		self.destB = destB

		self.button = Button(frame, text="Quit", fg="red", command=frame.quit)
		self.button.pack(side=LEFT)
		self.sortAButton = Button(frame, text="Sort to "+argv[2], command=self.sortA)
		self.sortAButton.pack(side=LEFT)
		self.sortBButton = Button(frame, text="Sort to "+argv[3], command=self.sortB)
		self.sortBButton.pack(side=LEFT)

		self.pic = PhotoImage(file=photo).subsample(5)
		self.label = Label(image=self.pic)
		self.label.image = self.pic # keep a reference!
		self.label.pack()
	def sortA(self):
		print("Send to", self.destA)
		self.f.quit()
	def sortB(self):
		print("Send to", self.destB)
		self.f.quit()

# photo = PhotoImage(file="image.gif")
# testImage = Image.open(argv[1])
testImage = file=argv[1]

root = Tk()
app = App(root, testImage, argv[2], argv[3])

root.mainloop()
root.destroy()
