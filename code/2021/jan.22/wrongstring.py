import time
import random
from PIL import Image as im, ImageDraw as idraw, ImageFont as ifont

class WrongString():
	"Generating some lines of text"

	def __init__(self, w, h, message, fontPath, fontSize, paintPath, iterations, breaks):
		self.w = w
		self.h = h
		self.fileName = WrongString.buildFileName(message)
		self.m = WrongString.buildString(message, iterations, breaks)
		self.font = ifont.truetype(fontPath, fontSize)
		self.canvas = im.new("RGB", (self.w, self.h), (255,255,255))
		self.paint = im.open(paintPath).resize(self.canvas.size)
		self.draw = idraw.Draw(self.canvas)
		print(self)
		WrongString.writeMessage(self)
		WrongString.buildImage(self)

	def buildString(message, iterations, breaks):
		print("-- building a character chain...", end="\r")
		text = ""
		for l in range(iterations):
			text += ''.join(random.sample(message, len(message)))
			if l % breaks == breaks - 1:
				text += "\n"
		print("-- the chain is ready!             ", end="\n")
		return text

	def writeMessage(self):
		self.draw.text((-10,-10), self.m, font=self.font, fill=(0,0,0))

	def buildImage(self):
		backImage = im.new("RGB", self.canvas.size, WrongString.buildBackground())
		new = im.composite(backImage, self.paint, self.canvas.convert("L"))
		new.save("output/" + self.fileName + ".jpg")
		print("-- the image was saved!", end="\n")

	def buildBackground():
		g = random.randint(0,50)
		return (g, g, g)

	def buildFileName(name):
		file = name.replace(" ", "")
		t = time.localtime()
		file += "_" + str(t[3]) + str(t[4]) + str(t[5])
		return file

	def __str__(self):
		return "-- wrongstring --\n" + \
				"-- https://gitlab.com/rodrigovalla/genuary2021\n" + \
				"-- version: 0.50\n" + \
				"-- Some work to be part of #genuary2021"
