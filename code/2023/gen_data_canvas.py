import numpy as np
from PIL import Image as im

class NCanvas():
	"The canvas to draw with pixels for genuary..."

	def __init__(self, width, height, background):
		self.background = background
		self.w = width
		self.h = height
		self.data = np.full((self.h, self.w, 3), self.background)

	#Setting up pixels colors...
	def paint_pixel(self, color, x, y, width):
		for i in range(width):
			self.paint_pixel(color, i+x, i+y)

	#Setting up a pixel color...
	def paint_pixel(self, color, x, y):
		self.data[y][x] = color

	#Inverting a pixel color...
	def invert_pixel(self, x, y):
		self.data[y][x][0] = 255 - self.data[y][x][0]
		self.data[y][x][1] = 255 - self.data[y][x][1]
		self.data[y][x][0] = 255 - self.data[y][x][2]

	#Returning a pixel color...
	def get_pixel_color(self, x, y):
		return self.data[y][x]

	#Returning a pixel color inverted...
	def get_inverted_pixel_color(self, x, y):
		r = 255 - self.data[y][x][0]
		g = 255 - self.data[y][x][1]
		b = 255 - self.data[y][x][2]
		return [r,g,b]

	#Loading image to canvas...
	def load_data(self, image_path):
		image = im.open(image_path).resize((self.data.shape[1], self.data.shape[0]))
		self.data = np.array(image)

	#Function to save image...
	def save(self, filepath, filename):
		data = np.array(np.round(self.data), dtype="uint8")
		image = im.fromarray(data)
		image.save(filepath + filename + ".jpg")

	#Function to show image...
	def show(self):
		data = np.array(np.round(self.data), dtype="uint8")
		image = im.fromarray(data)
		image.show()
