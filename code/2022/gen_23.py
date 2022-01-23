import math
import random as rd
from gen_color import GenColor
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen23():
	"The class to create abstract vegetation..."

	def __init__(self, active_width, active_height, margins, background, colors, color_motion, field_steps, line_w,
					angle_var, floor, lines):
		self.margins = margins
		self.background = background
		self.hw = [active_height, active_width]
		self.canvas = DCanvas(self.hw[1] + self.margins[1] * 2, self.hw[0] + self.margins[0] * 2, background)
		self.colors = [GenColor(c) for c in colors]
		self.lw = line_w
		self.field_steps = field_steps
		self.floor = floor
		self.lines = lines
		self.field = self.load_field(angle_var)
		self.paint(color_motion)

	def load_field(self, angle_var):
		field = []
		for y in range(self.field_steps[0]):
			a = 0 
			list = []
			a += y/self.field_steps[0] * angle_var[0]
			for x in range(self.field_steps[1]):
				a += (self.field_steps[0] // 15 + x)/self.field_steps[0] * angle_var[1]
				list.append(a)
			field.append(list)
		return field

	def paint(self, color_motion):
		distance = self.hw[0] / self.lines
		for l in range(self.lines):
			p = (rd.randint(0,self.hw[1]), rd.randint(self.hw[0]//3,self.hw[0]))
			t = 0
			while t < 1000:
				if self.is_point_in(p):
					a = self.look_for_angle(p)
					np = self.get_new_point(p, a, 2)
					active_color = self.decide_color(np[1])
					self.colors[active_color].move(color_motion)
					self.canvas.draw_line(self.colors[active_color].c, self.lw, (p[0]+self.margins[1],p[1]+self.margins[0]), (np[0]+self.margins[1],np[1]+self.margins[0]))
					p = np
				t += 1

	def decide_color(self, y):
		if y < self.floor:
			return 0
		else:
			return 1

	def look_for_angle(self, point):
		x = math.floor(point[0] / self.hw[1] * (self.field_steps[1] - 1))
		y = math.floor(point[1] / self.hw[0] * (self.field_steps[0] - 1))
		return self.field[y][x]

	def is_point_in(self, point):
		is_in = True
		if (point[0] < 0 or point[0] > self.hw[1] or point[1] < 0 or point[1] > self.hw[0]):
			is_in = False
		return is_in

	def get_new_point(self, last_point, angle, scale):
		x = math.cos(angle) * scale
		y = math.sin(angle) * scale
		return (last_point[0] + x, last_point[1] + y)
