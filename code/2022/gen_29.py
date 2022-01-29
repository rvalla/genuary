import math
import random as rd
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen29():
	"The class to make a pile of figures..."

	def __init__(self, active_width, active_height, margins, background, colors, color_motion, direction, noise_factor,
					size, piles, levels, threshold):
		self.hw = (active_height, active_width)
		self.margins = margins
		self.threshold = threshold
		self.direction = (direction[0] * self.hw[1], -(direction[1] * (self.hw[0] - size)) / levels)
		self.offset = self.hw[1] // (piles + 1)
		self.location = [self.offset + margins[1], self.hw[0] - size / 2 + margins[0]]
		self.size = size
		self.noise = 0
		self.noise_factor = noise_factor
		self.colors = colors
		self.color_count = len(colors)
		self.active_color = 0
		self.canvas = DCanvas(self.hw[1] + self.margins[1] * 2, self.hw[0] + self.margins[0] * 2, background)
		self.draw_pile(piles, levels, color_motion)

	def draw_pile(self, piles, levels, color_motion):
		for l in range(levels):
			for p in range(piles):
				point = (self.location[0] + self.offset * p, self.location[1])
				if rd.random() > self.threshold:
					self.canvas.draw_circle(self.colors[self.active_color], point, self.get_size(l))
			self.update()
			self.colors[self.active_color] = ut.move_color(self.colors[self.active_color], color_motion)
			self.active_color = (self.active_color + 1)%self.color_count

	def update(self):
		self.update_noise()
		self.location[0] += self.direction[0]
		self.location[1] += self.direction[1]

	def update_noise(self):
		self.noise += (rd.random()-0.5) * self.noise_factor

	def get_size(self, count):
		return self.size * (1 + (rd.random() * self.noise_factor - self.noise_factor / 2))
