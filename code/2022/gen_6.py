import math
import random as rd
from PIL import Image as im
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen6():
	"The class to try Antonio Sánchez Chinchón straight lines style..."

	def __init__(self, active_width, active_height, margins, background, color, signal_A, signal_B, signal_res,
				offset, scale, palette, speed):
		self.hw = (active_height, active_width)
		self.margins = margins
		self.color = color
		self.canvas = DCanvas(self.hw[1] + margins[1] * 2, self.hw[0] + margins[0] * 2, background)
		self.signal_A = signal_A
		self.signal_B = signal_B
		self.signal_width = round(active_width - offset)
		self.signal_resolution = signal_res
		self.scale = scale
		self.offset = offset
		self.paint(background, palette, speed)

	def paint(self, background, palette, speed):
		signal_A_h = self.hw[0] // 3
		signal_B_h = 2 * signal_A_h
		c = self.color
		for l in range(self.signal_width):
			x1 = l + self.margins[1]
			x2 = l + self.offset + self.margins[1]
			y1 = signal_A_h + self.get_signal_y(self.signal_A, self.signal_resolution * l) + self.margins[0]
			y2 = signal_B_h + self.get_signal_y(self.signal_B, self.signal_resolution * l) + self.margins[0]
			self.canvas.draw_line(c, 0, (x1,y1), (x2,y2))
			if palette:
				c = ut.move_color(c, 2)
			c = ut.color_grading(c, background, speed)

	def get_signal_y(self, signal, angle):
		y = 0
		for s in signal:
			y += math.sin(s[0] * (angle + s[2])) * s[1] * self.scale
		return y
