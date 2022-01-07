import math
import random as rd
from PIL import Image as im
from gen_color import GenColor
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen7():
	"The class to paint as Sol LeWitt in a wall..."

	def __init__(self, active_width, active_height, margins, background, color, points, line_w):
		self.hw = (active_height, active_width)
		self.margins = margins
		self.color = GenColor(color)
		self.canvas = DCanvas(self.hw[1] + margins[1] * 2, self.hw[0] + margins[0] * 2, background)
		self.lw = line_w
		self.points = self.load_points(points)
		self.paint(background)

	def paint(self, background):
		for p1 in range(len(self.points)):
			for p2 in self.points[p1:]:
				self.canvas.draw_line(self.color.c, self.lw, self.points[p1], p2)
				self.color.translate(2)

	def load_points(self, points):
		xs = rd.sample(range(0,self.hw[1]),points)
		ys = rd.sample(range(0,self.hw[0]),points)
		list = []
		for x, y in zip(xs, ys):
			list.append((self.margins[1] + x, self.margins[0] + y))
		return list
