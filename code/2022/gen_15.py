import random as rd
from gen_color import GenColor
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas
from gen_pendulum import GenPendulum

ut = GenUtil()

class Gen15():
	"The class to make a pendulum to draw with sand..."

	def __init__(self, active_width, active_height, background, color, color_motion, center, initial_position,
					initial_velocity, g_constant, degrades, windy, wind_range, times, grains):
		self.hw = (active_height, active_width)
		self.color = GenColor(color)
		self.pendulum = GenPendulum(center, initial_position, initial_velocity, g_constant, degrades, 1/(times*5))
		self.windy = windy
		self.wind = [0,0] #The wind moves the falling sand...
		self.wind_range = wind_range
		self.canvas = DCanvas(self.hw[1], self.hw[0], background)
		self.oscillation(color_motion, times, grains)

	def oscillation(self, color_motion, times, grains):
		for t in range(times):
			self.pendulum.update()
			self.drop_sand(grains)
			self.color.move(color_motion)
			if self.windy:
				self.update_wind()

	def drop_sand(self, grains):
		for g in range(grains): #dropping grains in each position...
			noise_x = g * (rd.random() * 10 - 5) + self.wind[0]
			noise_y = g * (rd.random() * 10 - 5) + self.wind[1]
			x = self.pendulum.p[0] + noise_x
			y = self.pendulum.p[1] + noise_y
			self.canvas.draw_point(self.color.c, (x,y))

	def update_wind(self):
		self.wind[0] += rd.random() * self.wind_range[0] - self.wind_range[0] / 2
		self.wind[1] += rd.random() * self.wind_range[1] - self.wind_range[1] / 2
