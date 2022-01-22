import random as rd
from gen_color import GenColor
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas
from PIL import ImageFont as ifont, ImageStat as istat

ut = GenUtil()

class Gen21():
	"The class to make something combining Gen19 and Gen1..."

	def __init__(self, active_width, active_height, margins, background, light, colors, color_motion, threshold,
					levels, size_factor, start_density, start_size):
		self.hw = (active_height, active_width)
		self.margins = margins
		self.cells = [1,1]
		self.cells_state = [[1]]
		self.cell_size = [active_height / self.cells[0], active_width / self.cells[1]]
		self.threshold = threshold
		self.levels = levels
		self.size = start_size
		self.size_factor = size_factor
		self.density = start_density
		self.colors = colors
		self.background_light = light
		self.canvas = DCanvas(self.hw[1] + self.margins[1] * 2, self.hw[0] + self.margins[0] *  2, background)
		self.build(color_motion)

	def build(self, color_motion):
		for l in range(self.levels):
			print("Processing level " + str(l+1) + "...", end="\r")
			for h in range(self.cells[0]):
				for w in range(self.cells[1]):
					if self.cells_state[h][w] == 1:
						f = [rd.choice([13,17,19,23]),0]
						self.draw(h, w, self.size, self.colors[l%len(self.colors)], color_motion, f)
			self.update_cells()
			self.evaluate(self.colors[l%len(self.colors)])
			self.size = [self.size[0] // 2, self.size[1] // 2]
		print("Done!                     ", end="\n")

	def evaluate(self, color):
		for h in range(self.cells[0]):
			for w in range(self.cells[1]):
				x = w * self.cell_size[1] + self.margins[1]
				y = h * self.cell_size[0] + self.margins[0]
				image = self.canvas.canvas.crop((x,y,x+self.cell_size[1],y+self.cell_size[0]))
				self.decide_cell(h,w,istat.Stat(image).mean)

	def decide_cell(self, h, w, mean):
		value = (mean[0] + mean[1] + mean[2]) / 3
		if self.background_light:
			if 255 - value > self.threshold:
				self.cells_state[h][w] = 1
		else:
			if value > self.threshold:
				self.cells_state[h][w] = 1

	def draw(self, h, w, size, color, color_motion, factors):
		x = w * self.cell_size[1] + self.margins[1]
		y = h * self.cell_size[0] + self.margins[0]
		ut.gen_rectangle(self.canvas, self.size[0], self.size[1], (y,x), self.density, [color], color_motion, factors, self.size_factor, True)

	def update_cells(self):
		self.cells = [2 * self.cells[0], 2 * self.cells[0]]
		self.cell_size = [self.hw[0] / self.cells[0], self.hw[1] / self.cells[1]]
		self.cells_state = []
		for r in range(self.cells[0]):
			self.cells_state.append([0 for i in range(self.cells[1])])
