import math
import random as rd
from PIL import Image as im
from gen_color import GenColor
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen7B():
	"The class to paint as Sol LeWitt in a wall..."

	def __init__(self, active_width, active_height, margins, background, color, lines, line_w):
		self.hw = (active_height, active_width)
		self.jump = active_width / lines
		self.lines = self.get_lines(lines, self.jump)
		self.margins = margins
		self.color = GenColor(color)
		self.canvas = DCanvas(self.hw[1] + margins[1] * 2, self.hw[0] + margins[0] * 2, background)
		self.lw = line_w
		self.paint()

	def paint(self):
		noise = rd.randint(0,self.hw[1]//70) - self.hw[1]//70 // 2
		a1 = self.hw[1] // 5 + noise
		a2 = a1 * 4 + noise
		for h in range(self.lines[1]):
			y = self.jump * h + self.margins[0]
			self.canvas.draw_line(self.color.c, self.lw, (a1 + self.margins[1],y), (a2 + self.margins[1],y))
			self.color.translate(2)
		self.color.reset()
		self.color.invert()
		noise = rd.randint(0,self.hw[1]//70) - self.hw[1]//70 // 2
		a1 = self.hw[0] // 5 + noise
		a2 = a1 * 4 + noise
		for w in range(self.lines[0]):
			x = self.jump * w + self.margins[1]
			self.canvas.draw_line(self.color.c, self.lw, (x, a1 + self.margins[0]), (x, a2 + self.margins[0]))
			self.color.translate(2)

	def get_lines(self, lines, jump):
		l = []
		l.append(int(lines))
		l.append(int(self.hw[0] // jump))
		return l
