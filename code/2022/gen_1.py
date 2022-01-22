import random as rd
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen1():
	"The class to create something drawing a thing 10.000 times..."

	def __init__(self, active_width, active_height, margins, background, colors, color_motion, factors,
					size_factor, constant_size):
		self.hw = [active_height, active_width]
		self.margins = margins
		self.canvas = DCanvas(self.hw[1] + margins[1] * 2, self.hw[0] + margins[0] * 2, background)
		self.colors = colors
		ut.gen_alpha_rectangle(self.canvas, self.hw[1], self.hw[0], self.margins, [100,100], self.colors, color_motion,
							factors, size_factor, constant_size)
