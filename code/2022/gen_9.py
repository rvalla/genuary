import random as rd
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen9():
	"The class to draw a minimal skyline..."

	def __init__(self, active_width, active_height, margins, background, color, color_motion, windows_colors,
					windows_density, constant_windows, buildings, night):
		self.hw = (active_height, active_width)
		self.night = night
		self.margins = margins
		self.colors = [color[0], color[1]]
		self.canvas = DCanvas(self.hw[1] + margins[1] * 2, self.hw[0] + margins[0] * 2, background)
		self.buildings = buildings
		self.b_widths, self.b_heights = self.building_heights(buildings)
		self.skyline(buildings, color_motion)
		self.fill_buildings(buildings, color_motion, windows_colors, constant_windows)

	def skyline(self, buildings, color_motion):
		x = self.margins[1] + self.hw[1] / 2
		y = self.margins[0] + self.hw[0] / 2
		self.canvas.draw_rectangle(self.colors[0], (x,y), (self.hw[1], self.hw[0]))
		for b in range(1, buildings + 1):
			x = self.b_widths[b-1] * b - self.b_widths[b-1] / 2 + self.margins[1]
			y = self.margins[0] + self.hw[0] - self.b_heights[b - 1] / 2
			self.canvas.draw_rectangle(self.colors[1], (x,y), (self.b_widths[b-1],self.b_heights[b-1]))
			self.colors[1] = ut.move_color(self.colors[1], color_motion)

	def fill_buildings(self, buildings, color_motion, windows_colors, constant_windows):
		h_margin = self.b_widths[0] / 10
		level_height = self.b_widths[0] / 2 - 2 * h_margin
		start_x = self.margins[1]
		start_y = 2 * self.margins[0] + self.hw[0]
		for b in range(buildings):
			levels = round(self.b_heights[b] // (level_height + h_margin))
			row = rd.choice([1,2,2,3,3,3,4])
			self.windows(start_x, start_y, levels, h_margin, level_height, self.b_widths[b], row, color_motion, windows_colors, constant_windows)
			start_x += self.b_widths[b]

	def windows(self, start_x, start_y, levels, margin, height, total_width, row, color_motion, windows_colors, constant_windows):
		width = self.windows_widths(margin, total_width, row)
		floor = self.hw[0] + self.margins[0]
		density = [rd.randint(3,6),rd.randint(5,10)]
		color = rd.choice(windows_colors)
		motion = rd.randint(color_motion // 2, color_motion)
		factors = [rd.choice([11,13,17,19]),rd.choice([0,0,0,17,19,23])]
		for r in range(row):
			x = start_x + margin + r * (width + margin)
			for l in range(levels):
				window_on = True
				if self.night:
					if rd.random() < 0.5:
						window_on = False
				if window_on:
					y = floor - margin - height - l * (height + margin)
					ut.gen_alpha_rectangle(self.canvas, width, height, [y,x], density, [color], motion, factors, 1, constant_windows)

	def windows_widths(self, margin, total_width, row):
		width = 0
		if row == 1:
			width = total_width - 2 * margin
		else:
			width = (total_width - margin) / row - margin
		return width

	def building_heights(self, buildings):
		bw = []
		step = self.hw[1] / buildings
		for w in range(buildings):
			bw.append(step)
		self.hw[1] / buildings
		bh = []
		min = self.hw[0] / 3
		step = self.hw[0] / 9
		if buildings > 6:
			heights = 6
		else:
			heights = buildings
		hs = rd.sample(range(0,6),heights)
		for i in range(buildings):
			bh.append(hs[i%len(hs)] * step + min)
		return bw, bh
