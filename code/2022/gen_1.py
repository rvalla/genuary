import random as rd
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen1():
	"The class to create something drawing a thing 10.000 times..."

	def __init__(self, width, height, background, colors, factors, sizefactor, margins):
		self.wh = [width, height]
		self.margins = margins
		self.steps = [(width - margins[0] * 2) / 100, (height - margins[1] * 2) / 100]
		self.thingwh = [self.steps[0] * 1, self.steps[1] * 1]
		self.canvas = DCanvas(width,height,background)
		self.colors = colors
		self.build(factors[0], factors[1])

	#Building the piece...
	def build(self, fx, fy):
		color_count = len(self.colors)
		active_color = rd.randint(0,color_count-1)
		size = self.thingwh
		for i in range(100):
			c = self.colors[(active_color)%color_count]
			size = (size[0] , (self.thingwh[1] + i%(7*self.steps[1])))
			for j in range(100):
				x = self.margins[0] + self.steps[0] / 2 + (j * fx)%100 * self.steps[0]
				y = self.margins[1] + self.steps[1] / 2 + (i * fy + j * fx)%100 * self.steps[1]
				center = (x, y)
				size = (self.thingwh[0] + j%(7*self.steps[0]), size[1])
				self.canvas.draw_rectangle(c, center, size)
				c = ut.move_color(c, 1)
			self.colors[(active_color+i)%color_count] = c
