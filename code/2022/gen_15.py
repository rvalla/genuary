import random as rd
import math
from gen_color import GenColor
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas
from gen_pendulum import GenPendulum

ut = GenUtil()

class Gen15():
	"The class to make a pendulum to draw with sand..."

	def __init__(self, active_width, active_height, background, color, color_motion, center, initial_position,
					initial_velocity, g_constant, degrades, windy, wind_range, times, grains, drop_mode, drop_radious_ratio):
		self.hw = (active_height, active_width)
		self.drop_mode = drop_mode
		self.drop_radious = round(active_width * drop_radious_ratio)
		self.color = GenColor(color)
		self.pendulum = GenPendulum(center, initial_position, initial_velocity, g_constant, degrades, 1/(times*200))
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
			noise_x, noise_y = self.grain_noise()
			x = self.pendulum.p[0] + noise_x
			y = self.pendulum.p[1] + noise_y
			self.canvas.draw_point(self.color.c, (x,y))

	def grain_noise(self):
		noise_x = 0.0
		noise_y = 0.0
		if self.drop_mode == "square":
			noise_x = (rd.random() * self.drop_radious - self.drop_radious/2) + self.wind[0]
			noise_y = (rd.random() * self.drop_radious - self.drop_radious/2) + self.wind[1]
		elif self.drop_mode == "circle":
			if rd.random() < 0.5:
				x = min(rd.random(), rd.random()) * self.drop_radious
				y = rd.random() * (math.sqrt(self.drop_radious*self.drop_radious - x*x))
			else:
				y = min(rd.random(), rd.random()) * self.drop_radious
				x = rd.random() * (math.sqrt(self.drop_radious*self.drop_radious - y*y))
			noise_x = x * rd.choice([-1,1]) + self.wind[0]
			noise_y = y * rd.choice([-1,1]) + self.wind[1]
		return noise_x, noise_y

	def update_wind(self):
		self.wind[0] += rd.random() * self.wind_range[0] - self.wind_range[0] / 2
		self.wind[1] += rd.random() * self.wind_range[1] - self.wind_range[1] / 2
