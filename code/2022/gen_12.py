import random as rd
import math
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen12():
	"The class to get a pack of polygons..."

	def __init__(self, active_width, active_height, margins, background, color, color_motion, levels, centers, line_w, scales):
		self.hw = (active_height, active_width)
		self.margins = margins
		self.centers = self.build_centers(centers, margins)
		self.scales = scales
		self.color = color
		self.line_w = line_w
		self.polygons = self.create_polygons(self.centers, scales, color)
		self.canvas = DCanvas(self.hw[1] + margins[1] * 2, self.hw[0] + margins[0] * 2, background)
		self.pack(levels, color_motion)

	def pack(self, levels, color_motion):
		for l in range(levels):
			self.draw_polygons()
			self.update_polygons()
			self.color = ut.move_color(self.color, color_motion)

	def update_polygons(self):
		for p in self.polygons:
			p.s = [p.s[0] * 0.75, p.s[1] * 0.75]
			p.mutation()

	def create_polygons(self, centers, scales, color):
		p = []
		for c in centers:
			p.append(GenPolygon(c, rd.randint(3,11), color, scales))
		return p

	def draw_polygons(self):
		for p in self.polygons:
			self.canvas.draw_empty_polygon(self.color, self.line_w, p.p)

	def build_centers(self, centers, margins):
		c = []
		for i in centers:
			c.append((i[0] + margins[1], i[1] + margins[0]))
		return c
