import random as rd
import math
from gen_color import GenColor
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen16():
	"The class to make a color gradient go wrong..."

	def __init__(self, active_width, active_height, margins, background, color, color_motion, signal, scale, lines,
					lines_height):
		self.hw = (active_height, active_width)
		self.margins = margins
		self.signal = signal
		self.scale = scale
		self.lines_h = lines_height
		self.color = GenColor(color)
		self.color.d = self.set_color_directions()
		self.axis = self.hw[0] // 2 + self.margins[0]
		self.canvas = DCanvas(self.hw[1] + self.margins[1] * 2, self.hw[0] + self.margins[0] *  2, background)
		self.draw_lines(lines, color_motion)

	def draw_lines(self, lines, color_motion):
		step = self.hw[1] // lines
		y_offset = self.axis - self.lines_h // 2
		signal_resolution = self.hw[1] / lines * 0.05
		for l in range(lines):
			x = l*step + self.margins[1]
			y = - self.get_signal_y(self.signal, l * signal_resolution) + y_offset
			self.canvas.draw_line(self.color.c, 0, (x,y), (x,y+self.lines_h))
			self.color.independent_overflow(color_motion)

	def set_color_directions(self):
		r = rd.choice([-1,1])
		g = rd.choice([-1,1])
		b = rd.choice([-1,1])
		return [r,g,b]

	def get_signal_y(self, signal, angle):
		y = 1
		for s in signal:
			y += math.sin(s[0] * (angle + s[2])) * s[1] * self.scale
		return y
