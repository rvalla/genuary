import math
import random as rd
import numpy as np
from PIL import Image as im
from gen_pixel import GenPixel
from gen_virus import GenVirus
from gen_util import GenUtil
from gen_data_canvas import NCanvas

ut = GenUtil()

class Gen3():
	"The class to create something with space..."

	def __init__(self, active_width, active_height, margins, background, virus_colors, virus_thresholds, contacts_width, days):
		self.margins = margins
		self.background = background
		self.hw = [active_height, active_width]
		self.canvas = NCanvas(self.hw[1] + self.margins[1] * 2, self.hw[0] + self.margins[0] * 2, background)
		self.age = 0
		self.days = days
		self.virus_thresholds = virus_thresholds
		self.virus_count = None
		self.virus = []
		self.pixels = []
		self.simulate(virus_colors, contacts_width)
		self.paint_result()

	#Simulating an epidemic...
	def simulate(self, virus_colors, contacts_width):
		self.start_epidemic(virus_colors, contacts_width)
		print("Ready to simulate the epidemic...", end="\n")
		while self.age < self.days:
			print("Simulating day " + str(self.age), end="\r")
			self.simulate_day()

	#Painting the result...
	def paint_result(self):
		print("Painting result..." + str(self.age), end="\r")
		for h in range(self.hw[0]):
			for w in range(self.hw[1]):
				self.canvas.paint_pixel(self.pixels[h][w].c, w + self.margins[1], h + self.margins[0])
		print("Result is ready...", end="\n")

	#Starting the epidemic...
	def start_epidemic(self, virus_colors, contacts_width):
		for v in range(len(virus_colors)):
			t = rd.uniform(self.virus_thresholds[0],self.virus_thresholds[1])
			m = rd.randint(2,5)
			d = rd.randint(3,8)
			c = rd.randint(0,contacts_width)
			contacts = (c - contacts_width, c)
			self.virus.append(GenVirus(virus_colors[v], contacts, t, m, d))
		self.virus_count = len(self.virus)
		for h in range(self.hw[0]):
			l = []
			for w in range(self.hw[1]):
				l.append(GenPixel(w,h,self.background))
			self.pixels.append(l)
		center = (self.hw[0] // 2, self.hw[1] // 2)
		radius = (self.hw[0] // 4, self.hw[1] // 4)
		angle = math.pi * 2 / self.virus_count
		rotation = rd.random() * 3
		if self.virus_count > 1:
			for i in range(self.virus_count):
				x = round(center[1] + math.cos(angle * i + rotation) * radius[1])
				y = round(center[0] + math.sin(angle * i + rotation) * radius[0])
				self.pixels[y][x].infection(self.virus[i%self.virus_count], i%self.virus_count)
		else:
			self.pixels[center[0]][center[1]].infection(self.virus[0], 0)

	#Simulating a day...
	def simulate_day(self):
		infected_pixels = self.infected_list()
		for p in infected_pixels:
			v = self.pixels[p[0]][p[1]].virus_id
			limits = self.virus[v].contacts
			for i in range(limits[0],limits[1]):
				for j in range(limits[0],limits[1]):
					t = rd.random()
					if t < self.virus[v].threshold:
						x = p[1] + j
						y = p[0] + i
						if y >= 0 and y < self.hw[0] and x >= 0 and x < self.hw[1]:
							self.pixels[y][x].infection(self.virus[v], v)
			self.pixels[p[0]][p[1]].update()
		for v in self.virus:
			v.update()
		self.age += 1

	#Building infected pixels list...
	def infected_list(self):
		l = []
		for h in range(self.hw[0]):
			for w in range(self.hw[1]):
				if self.pixels[h][w].is_infected:
					l.append((h,w))
		return l
