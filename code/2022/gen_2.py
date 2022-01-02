import random as rd
import numpy as np
from PIL import Image as im
from gen_util import GenUtil
from gen_data_canvas import NCanvas

ut = GenUtil()

class Gen2():
	"The class to create something using dithering..."

	def __init__(self, image_path, border, margins, background):
		self.input = np.array(im.open(image_path))
		self.margins = margins
		self.background = background
		self.hw = [self.input.shape[1] + margins[1] * 2, self.input.shape[0] + margins[0] * 2]
		self.canvas = NCanvas(self.hw[0],self.hw[1],background)
		self.border = border
		self.build(self.border)

	#Building the piece...
	def build(self, b):
		for r in range(self.input.shape[0]):
			channel = rd.choice([0,1,2])
			for c in range(self.input.shape[1]):
				color = self.input[r][c]
				v = color[channel]
				if v < b:
					v = 0
				else:
					v = 255
				e = b - v
				color[channel] = v
				self.input[r][(c+1)%self.input.shape[1]][channel] += e
				self.input[(r+1)%self.input.shape[0]][c][channel] += e * 0.5
				self.canvas.paint_pixel(color, c + self.margins[0], r + self.margins[1])
