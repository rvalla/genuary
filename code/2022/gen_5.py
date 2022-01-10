import random as rd
from PIL import Image as im
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas
from gen_1 import Gen1

ut = GenUtil()

class Gen5(Gen1):
	"The class to destroy a square..."

	def __init__(self, active_width, active_height, margins, background, colors, color_motion, factors, sizefactor,
					constant_size, cuts, cuts_width):
		Gen1.__init__(self, active_width, active_height, margins, background, colors, color_motion, factors, sizefactor, constant_size)
		self.color = background
		self.cuts = self.load_cuts(cuts, self.canvas.hw[1], self.canvas.hw[0])
		self.cuts_width = cuts_width
		self.cuts_noise = (self.hw[0] // 10, self.hw[1] // 10)
		self.destroy(1)
		self.destroy(0)

	def destroy(self, x):
		y = (x + 1) % 2
		as1 = rd.sample(range(self.canvas.hw[x]), self.cuts[x])
		as2 = rd.sample(range(self.canvas.hw[x]), self.cuts[x])
		as1.sort()
		as2.sort()
		b1 = 0 + rd.randint(0, self.cuts_noise[y])
		b2 = self.canvas.hw[y] - b1
		for a1, a2 in zip(as1,as2[::-1]):
			if y == 0:
				self.canvas.draw_line(self.color, self.cuts_width, (a1,b1), (a2,b2))
			elif y == 1:
				self.canvas.draw_line(self.color, self.cuts_width, (b1, a1), (b2, a2))

	def load_cuts(self, cuts, w, h):
		a = w / (w + h)
		cw = round(cuts * a)
		ch = cuts - cw
		return (ch, cw)
