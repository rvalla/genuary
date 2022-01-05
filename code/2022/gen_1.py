import random as rd
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen1():
	"The class to create something drawing a thing 10.000 times..."

	def __init__(self, active_width, active_height, margins, background, colors, factors, sizefactor, constant_size):
		self.hw = [active_height, active_width]
		self.margins = margins
		self.steps = [self.hw[0] / 100, self.hw[1] / 100]
		self.thinghw = [self.steps[1] * sizefactor, self.steps[0] * sizefactor]
		self.canvas = DCanvas(self.hw[1] + margins[1] * 2, self.hw[0] + margins[0] * 2, background)
		self.colors = colors
		self.build(factors[0], factors[1], constant_size)

	#Building the piece...
	def build(self, fx, fy, constant_size):
		color_count = len(self.colors)
		active_color = rd.randint(0,color_count-1)
		size = self.thinghw
		for i in range(100):
			active_color = (active_color+i)%color_count
			c = self.colors[active_color]
			if not constant_size:
				size = (size[0] , (self.thinghw[1] + i%(4*self.steps[1])))
			for j in range(100):
				x = self.margins[1] + self.steps[1] / 2 + (j * fx)%100 * self.steps[1]
				y = self.margins[0] + self.steps[0] / 2 + (j * fy + i * fx)%100 * self.steps[0]
				center = (x, y)
				if not constant_size:
					size = (self.thinghw[0] + j%(4*self.steps[0]), size[1])
				self.canvas.draw_rectangle(c, center, size)
				c = ut.move_color(c, 1)
			self.colors[active_color] = c
