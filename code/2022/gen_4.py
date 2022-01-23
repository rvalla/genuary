import math
import random as rd
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen4():
	"The class to create something with the next next Fidenza (Ok, I will try al least with a flow field)..."

	def __init__(self, active_width, active_height, margins, background, colors, field_type, field_steps,
					line_w, circle_d, angle_var, lines, circles):
		self.margins = margins
		self.background = background
		self.hw = [active_height, active_width]
		self.canvas = DCanvas(self.hw[1] + self.margins[1] * 2, self.hw[0] + self.margins[0] * 2, background)
		self.colors = colors
		self.circles = circles
		self.cd = circle_d
		self.lw = line_w
		self.field_steps = field_steps
		self.lines = lines
		self.field = self.load_field(field_type, angle_var)
		self.paint()

	def load_field(self, type, angle_var):
		if type == 0:
			field = self.load_curves(angle_var)
		elif type == 1:
			field = self.load_sin_x(angle_var)
		elif type == 2:
			field = self.load_fm(angle_var)
		return field

	def load_curves(self, angle_var):
		a = rd.random() * math.pi
		field = []
		for y in range(self.field_steps[0]):
			list = []
			a += y/self.field_steps[0] * angle_var[0]
			for x in range(self.field_steps[1]):
				a += x/self.field_steps[0] + angle_var[1]
				list.append(a)
			field.append(list)
		return field

	def load_sin_x(self, angle_var):
		a = 0.0
		field = []
		for y in range(self.field_steps[0]):
			list = []
			a += y/self.field_steps[0] * angle_var[0] + rd.random()
			for x in range(self.field_steps[1]):
				a += x/self.field_steps[0] + math.sin(x/math.pi) * angle_var[1]
				list.append(a)
			field.append(list)
		return field

	def load_fm(self, angle_var):
		a = 0.0
		field = []
		for y in range(self.field_steps[0]):
			list = []
			a += y/self.field_steps[0] * angle_var[0] + rd.random()
			for x in range(self.field_steps[1]):
				a += math.sin((x * math.sin(y/self.field_steps[0]))/math.pi) * angle_var[1]
				list.append(a)
			field.append(list)
		return field

	def paint(self):
		distance = self.hw[0] / self.lines
		for l in range(self.lines):
			p = (rd.randint(0,self.hw[1]), rd.randint(0,self.hw[0]))
			c_count = len(self.colors)
			for c in range(c_count):
				self.colors[c] = ut.move_color(self.colors[c], 5)
			t = 0
			offset = rd.randint(1,200)+200
			while t < 1000:
				if self.is_point_in(p):
					a = self.look_for_angle(p)
					if not self.circles:
						np = self.get_new_point(p, a, rd.randint(1,self.hw[0]//75))
						self.canvas.draw_line(self.colors[(t//offset)%c_count], self.lw, (p[0]+self.margins[1],p[1]+self.margins[0]), (np[0]+self.margins[1],np[1]+self.margins[0]))
					else:
						s = math.sin(0.1 * t) * self.cd
						np = self.get_new_point(p, a, s)
						self.canvas.draw_circle(self.colors[(t//offset)%c_count], (np[0]+self.margins[1],np[1]+self.margins[0]), s)
					p = np
				t += 1

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
