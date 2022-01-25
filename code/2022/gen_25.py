import random as rd
import math
from gen_color import GenColor
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen25():
	"The class to make a color gradient go wrong..."

	def __init__(self, active_width, active_height, margins, background, color, color_motion, signal, scale,
					step, perspective_data):
		self.hw = (active_height, active_width)
		self.margins = margins
		self.signal = signal
		self.scale = scale
		self.perspective_data = perspective_data #[min_height, max_height, step, whole_width, start_offset]
		self.perspective_state = [perspective_data[0], 0, 0] #line_height, growing state, counter
		self.color = GenColor(color)
		self.color.d = self.set_color_directions()
		self.axis = self.hw[0] // 2 + self.margins[0]
		self.vanishing_point = (self.margins[1],self.axis)
		self.canvas = DCanvas(self.hw[1] + self.margins[1] * 2, self.hw[0] + self.margins[0] *  2, background)
		self.draw_perspective(step, color_motion)

	def draw_perspective(self, step, color_motion):
		signal_resolution =  0.05
		l = 0
		while self.update_perspective():
			x = l*step + self.margins[1] + self.perspective_data[4]
			y_offset = self.axis - self.perspective_state[0] // 2
			y = - self.get_signal_y(self.signal, l * signal_resolution) + y_offset
			self.canvas.draw_line(self.color.c, 0, self.vanishing_point, (x,y))
			self.canvas.draw_line(self.color.c, 0, self.vanishing_point, (x,y+self.perspective_state[0]))
			self.color.independent_overflow(color_motion)
			l += 1

	def update_perspective(self):
		#Checking line height...
		if self.perspective_state[1] == 0:
			self.perspective_state[0] += self.perspective_data[2]
			if self.perspective_state[0] > self.perspective_data[1]:
				self.perspective_state[1] = 1
		elif self.perspective_state[1] == 1:
			if self.perspective_state[2] < self.perspective_data[3]:
				self.perspective_state[2] += 1
			else:
				self.perspective_state[1] = 2
				self.vanishing_point = (self.hw[1] + self.margins[1], self.axis)
		elif self.perspective_state[1] == 2:
			self.perspective_state[0] -= self.perspective_data[2]
		if self.perspective_state[0] < self.perspective_data[0]:
			return False
		else:
			return True

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
