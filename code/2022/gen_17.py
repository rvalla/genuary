import random as rd
from gen_color import GenColor
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen17():
	"The class to make something with 3 colors..."

	def __init__(self, active_width, active_height, margins, background, colors, lines_w, lines_h, loops, loop_size):
		self.hw = (active_height, active_width)
		self.margins = margins
		self.lines_h, self.lines_m, self.ys = self.get_y_data(lines_h)
		self.colors = [GenColor(c) for c in colors]
		self.canvas = DCanvas(self.hw[1] + self.margins[1] * 2, self.hw[0] + self.margins[0] *  2, background)
		self.draw_lines(loops, loop_size, lines_w)

	def draw_lines(self, loops, loop_size, lines_w):
		step = self.hw[1] / (loops * loop_size)
		for l in range(loops):
			offset = l * step * loop_size + self.margins[1] + step / 2
			for t in range(loop_size):
				x = t*step + offset
				for i in range(3):
					self.canvas.draw_line(self.colors[i].c, lines_w, (x,self.ys[i]), (x,self.ys[i]+self.lines_h))
			self.update_colors()

	def get_y_data(self, lines_h):
		ys = []
		margin = self.hw[0] / 3 - lines_h
		ys.append(self.margins[0] + margin / 2)
		ys.append(ys[0] + lines_h + margin)
		ys.append(ys[1] + lines_h + margin)
		return lines_h, margin, ys

	def update_colors(self):
		for c in range(3):
			self.colors[c].getting_close(self.colors[rd.choice([0,1,2])].c)
