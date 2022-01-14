import random as rd
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen13():
	"The class to get an hexagram of meta rectangles..."

	def __init__(self, active_width, active_height, margins, background, density, colors, color_motion,
					size_factor, constant_size):
		self.hw = (active_height, active_width)
		self.margins = margins
		self.colors = colors
		self.colors_count = len(colors)
		self.densities = [density, [density[0], round(density[1] * 0.4)]]
		self.canvas = DCanvas(self.hw[1] + margins[1] * 2, self.hw[0] + margins[0] * 2, background)
		self.hexagram(colors, color_motion, size_factor, constant_size)

	def hexagram(self, colors, color_motion, size_factor, constant_size):
		height = self.hw[0] / 11
		space = self.hw[1] / 5
		strips = self.get_strips()
		y = self.margins[0]
		for s in strips:
			factors = self.get_factors(s)
			color = colors[s%self.colors_count]
			location = [y, self.margins[1]]
			if s < 2:
				if s == 0:
					ut.gen_rectangle(self.canvas, self.hw[1], height, location, self.densities[0], [color], color_motion[0], factors, size_factor, constant_size)
				else:
					ut.gen_rectangle(self.canvas, self.hw[1], height, location, self.densities[0], [color], color_motion[1], factors, size_factor, constant_size)
			else:
				if s == 2:
					ut.gen_rectangle(self.canvas, 2 * space, height, location, self.densities[1], [color], color_motion[0], factors, size_factor, constant_size)
					location[1] += space * 3
					ut.gen_rectangle(self.canvas, 2 * space, height, location, self.densities[1], [color], color_motion[0], factors, size_factor, constant_size)
				else:
					ut.gen_rectangle(self.canvas, 2 * space, height, location, self.densities[1], [color], color_motion[1], factors, size_factor, constant_size)
					location[1] += space * 3
					ut.gen_rectangle(self.canvas, 2 * space, height, location, self.densities[1], [color], color_motion[1], factors, size_factor, constant_size)
			y += 2 * height

	def get_factors(self, case):
		primes = [13,17,19,23]
		return [primes[case], 0]

	def get_strips(self):
		strips = []
		for s in range(6):
			strips.append(self.flip_coins())
		return strips

	#John Cage used 3 coins to decide each line of an hexagram. Then mapped each hexagram to a table...
	def flip_coins(self):
		cs = 0
		for c in range(3):
			cs += self.flip_coin()
		return cs

	def flip_coin(self):
		return rd.choice([0,1])
