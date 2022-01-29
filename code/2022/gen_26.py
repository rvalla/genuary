import math
import random as rd
from gen_color import GenColor
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen26():
	"The class to make an airport carpet..."

	def __init__(self, active_width, active_height, background, colors, color_motion, grid, scale, noise_factor, levels):
		self.hw = (active_height, active_width)
		self.scale = scale
		self.angle = rd.random() * math.pi * 2
		self.grid = self.build_grid(grid)
		self.noise = (0,0)
		self.noise_factor = noise_factor
		self.color_count = len(colors)
		self.colors = [GenColor(c) for c in colors]
		self.canvas = DCanvas(self.hw[1], self.hw[0], background)
		self.draw_carpet(levels, color_motion)

	def draw_carpet(self, levels, color_motion):
		for l in range(levels):
			self.colors[l%self.color_count].move(color_motion)
			self.draw_grid(l, self.noise, self.colors[l%self.color_count].c)

	def draw_grid(self, level, noise, color):
		self.update_noise()
		for p in self.grid:
			size, radius = self.get_size_and_radius(p)
			self.canvas.draw_empty_rounded_rectangle(color, 3, (p[0]+level*noise[0],p[1]+level*noise[1]), size, radius)

	def build_grid(self, grid):
		g = []
		width = self.hw[1] / grid[1]
		height = self.hw[0] / grid[0]
		for r in range(grid[0] + 1):
			for c in range(grid[1] + 1):
				g.append((c * width, r * height))
		return g

	def update_noise(self):
		noise_x = (rd.random()-0.5) * self.noise_factor
		noise_y = (rd.random()-0.5) * self.noise_factor
		self.noise = (self.noise[0] + noise_x, self.noise[1] + noise_y)

	def get_size_and_radius(self, point):
		size = (self.scale * (math.sin(point[0] + self.angle) + 1),self.scale * (math.cos(point[1] + self.angle) + 1))
		radius = (size[0] + size[1]) / 50
		return size, radius
