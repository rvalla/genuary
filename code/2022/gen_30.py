import math
import random as rd
from PIL import Image as im
from gen_util import GenUtil
from gen_color import GenColor
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen30():
	"The class to draw with rectangles something organcic..."

	def __init__(self, active_width, active_height, margins, background, colors, color_motion, signal, signal_res, scale,
					lines, gap, lines_w, steps, base_size, grading, speed):
		self.hw = (active_height, active_width)
		self.margins = margins
		self.colors = [GenColor(c) for c in colors]
		self.color_count = len(self.colors)
		self.canvas = DCanvas(self.hw[1] + margins[1] * 2, self.hw[0] + margins[0] * 2, background)
		self.signal = signal
		self.signal_resolution = signal_res
		self.scale = scale
		self.axis = self.hw[0] // 2 + self.margins[0]
		self.base_size = base_size
		self.gap = gap * self.base_size[1]
		self.lw = lines_w
		self.paint(background, steps, lines, grading, speed, color_motion)

	def paint(self, background, steps, lines, grading, speed, color_motion):
		signal_h =  self.hw[0] / 2 - (self.gap * (lines-1))/2 - self.base_size[1] / 2 + self.margins[0]
		for l in range(lines):
			for s in range(steps):
				x = s * self.hw[1] // steps + self.margins[1]
				y = signal_h + self.get_signal_y(self.signal, self.signal_resolution * s)
				self.canvas.draw_empty_rectangle(self.colors[l%self.color_count].c, self.lw, (x,y), self.get_size(self.signal_resolution * s, l))
			signal_h += self.gap
			if grading:
				self.colors[l%self.color_count].degrade(background, speed)
			else:
				self.colors[l%self.color_count].move(color_motion)

	def get_size(self, step, line):
		if line%2 == 0:
			x = (0.5 + abs(math.cos(step))) * self.base_size[0]
			y = (0.5 + abs(math.cos(step))) * self.base_size[1]
		else:
			x = (0.5 + abs(math.sin(step))) * self.base_size[0]
			y = (0.5 + abs(math.sin(step))) * self.base_size[1]
		return (x,y)

	def get_signal_y(self, signal, angle):
		y = 0
		for s in signal:
			y += math.sin(s[0] * (angle + s[2])) * s[1] * self.scale
		return y
