from PIL import Image as im, ImageDraw as idraw

class DCanvas():
	"The canvas to draw with Pillow for genuary..."

	def __init__(self, width, height, background):
		self.background = background
		self.hw = [height,width]
		self.c = (self.hw[0]/2, self.hw[1]/2)
		self.canvas = im.new("RGB",(self.hw[1], self.hw[0]),self.background)
		self.draw = idraw.Draw(self.canvas)

	#Function to draw a point...
	def draw_point(self, c, p):
		self.draw.point(p, fill=c)

	#Function to draw a line...
	def draw_line(self, c, w, a, b):
		self.draw.line([a,b], fill=c, width=w)

	#Function to draw a circle...
	def draw_circle(self, color, center, d):
		a = (center[0] - d/2, center[1] - d/2)
		b = (center[0] + d/2, center[1] + d/2)
		self.draw.ellipse([a,b], fill=color, outline=None)

	#Function to draw a rectangle...
	def draw_rectangle(self, color, center, size):
		a = (center[0] - size[0]/2, center[1] - size[1] / 2)
		b = (a[0] + size[0], a[1] + size[1])
		self.draw.rectangle([a,b], fill=color, outline=None)

	#Function to draw an empty rectangle...
	def draw_empty_rectangle(self, border, width, center, size):
		a = (center[0] - size[0]/2, center[1] - size[1] / 2)
		b = (a[0] + size[0], a[1] + size[1])
		self.draw.rounded_rectangle([a,b], fill=None, outline=border, width=width)

	#Function to draw a rounded rectangle...
	def draw_rounded_rectangle(self, color, center, size, r):
		a = (center[0] - size[0]/2, center[1] - size[1] / 2)
		b = (a[0] + size[0], a[1] + size[1])
		self.draw.rounded_rectangle([a,b], radius=r, fill=color, outline=None)

	#Function to draw an empty rounded rectangle...
	def draw_empty_rounded_rectangle(self, border, width, center, size, r):
		a = (center[0] - size[0]/2, center[1] - size[1] / 2)
		b = (a[0] + size[0], a[1] + size[1])
		self.draw.rounded_rectangle([a,b], radius=r, fill=None, outline=border, width=width)

	#Function to write a message...
	def write(self, x, y, cell, message, font, color):
		self.draw.text((x,y), message, anchor="mm", font=font, fill=color)

	#Function to save the drawing...
	def save(self, filepath, filename):
		self.canvas.save(filepath + filename + ".jpg")
