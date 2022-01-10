import random as rd
import math
import sys
from gen_color import GenColor
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

sys.setrecursionlimit(10000)
ut = GenUtil()

class Gen10():
	"The class to get a machine learning wrong answer..."

	def __init__(self, active_width, active_height, margins, background, color, color_motion, lines, line_w, scale):
		self.hw = (active_height, active_width)
		self.margins = margins
		self.color = GenColor(color)
		self.line_w = line_w
		self.canvas = DCanvas(self.hw[1] + margins[1] * 2, self.hw[0] + margins[0] * 2, background)
		self.cum_angle = math.pi
		self.run(color_motion, lines, line_w, scale)

	def run(self, color_motion, lines, line_w, scale):
		y = self.hw[0] // 2 + self.margins[0] + rd.randint(0,self.margins[0])
		x = self.hw[1] // 3 + self.margins[1] + rd.randint(0,self.margins[1])
		for l in range(lines):
			self.draw_path((x,y), self.cum_angle, scale, line_w)
			self.color.translate(color_motion)

	def draw_path(self, origin, angle, scale, line_w):
		p = origin
		np = self.get_new_point(p, angle, scale)
		noise = rd.random() / 100 - 0.005
		while self.is_line_trap(np):
			self.canvas.draw_line(self.color.c, line_w, p, np)
			p = np
			np = self.get_new_point(p, angle, scale)
			angle += noise
		angle = self.turn(angle)
		if not self.is_line_out(np):
			self.draw_path(p, angle, scale, line_w)
		else:
			self.cum_angle -= angle

	def is_line_trap(self, p):
		if p[0] < self.margins[1] or p[1] < self.margins[0] or p[1] > self.margins[0] + self.hw[0]:
			return False
		else:
			return True

	def is_line_out(self, p):
		if p[0] > self.canvas.hw[1]:
			return True
		else:
			return False

	def turn(self, angle):
		return angle + rd.random() - 0.5

	def get_new_point(self, last_point, angle, scale):
		x = math.cos(angle) * scale
		y = math.sin(angle) * scale
		return (last_point[0] + x, last_point[1] + y)
