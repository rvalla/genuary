import random as rd
from gen_color import GenColor
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas
from PIL import ImageFont as ifont, ImageStat as istat

ut = GenUtil()

class Gen19():
	"The class to make something with text..."

	def __init__(self, active_width, active_height, margins, background, light, color, color_motion, threshold, word,
					font_path, font_size):
		self.hw = (active_height, active_width)
		self.margins = margins
		self.cells = [1,1]
		self.cells_state = [[1]]
		self.cell_size = [active_height / self.cells[0], active_width / self.cells[1]]
		self.threshold = threshold
		self.font_path = font_path
		self.font_size = font_size
		self.font = ifont.truetype(font_path, font_size)
		self.word = word
		self.color = GenColor(color)
		self.background_light = light
		self.canvas = DCanvas(self.hw[1] + self.margins[1] * 2, self.hw[0] + self.margins[0] *  2, background)
		self.build(color_motion)

	def build(self, color_motion):
		for l in self.word:
			print("Processing letter " + l + "...", end="\r")
			for h in range(self.cells[0]):
				for w in range(self.cells[1]):
					if self.cells_state[h][w] == 1:
						self.write(h, w, l, self.font_size, self.color.c)
			self.update_cells()
			self.evaluate(self.color.c)
			self.color.move(color_motion)
			self.font_size = self.font_size // 2
			self.font = ifont.truetype(self.font_path, self.font_size)
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

	def write(self, h, w, letter, size, color):
		x = w * self.cell_size[1] + self.margins[1] + self.cell_size[1] / 2
		y = h * self.cell_size[0] + self.margins[0] + self.cell_size[0] / 2
		self.canvas.write(x, y, self.cell_size, letter, self.font, color)

	def update_cells(self):
		self.cells = [2 * self.cells[0], 2 * self.cells[0]]
		self.cell_size = [self.hw[0] / self.cells[0], self.hw[1] / self.cells[1]]
		self.cells_state = []
		for r in range(self.cells[0]):
			self.cells_state.append([0 for i in range(self.cells[1])])
