import math
import random as rd
from PIL import Image as im
from gen_util import GenUtil
from gen_color import GenColor
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen8():
	"The class to draw a single curve..."

	def __init__(self, active_width, active_height, margins, background, color, signal, signal_res, scale, lines,
					grading, speed):
		self.hw = (active_height, active_width)
		self.margins = margins
		self.color = GenColor(color)
		self.canvas = DCanvas(self.hw[1] + margins[1] * 2, self.hw[0] + margins[0] * 2, background)
		self.signal = signal
		self.signal_width = self.hw[1]
		self.signal_resolution = signal_res
		self.scale = scale
		self.paint(background, lines, grading, speed)

	def paint(self, background, lines, grading, speed):
		signal_h = self.hw[0] // 2
		c = self.color
		for l in range(lines):
			for s in range(self.signal_width):
				x = s + self.margins[1]
				y = signal_h + self.get_signal_y(self.signal, self.signal_resolution * s) + self.margins[0]
				self.canvas.draw_point(self.color.c, (x,y))
			signal_h += 1
			if grading:
				self.color.degrade(background, speed)
			else:
				self.color.translate(10)

	def get_signal_y(self, signal, angle):
		y = 0
		for s in signal:
			y += math.sin(s[0] * (angle + s[2])) * s[1] * self.scale
		return y
