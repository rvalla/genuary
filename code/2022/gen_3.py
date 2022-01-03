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

	def __init__(self, active_width, active_height, margins, background, virus_colors, virus_thresholds, days):
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
		self.simulate(virus_colors)
		self.start_epidemic(virus_colors)
		self.paint_result()

	#Simulating an epidemic...
	def simulate(self, virus_colors):
		self.start_epidemic(virus_colors)
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
	def start_epidemic(self, virus_colors):
		for v in range(len(virus_colors)):
			t = rd.uniform(self.virus_thresholds[0],self.virus_thresholds[1])
			m = rd.randint(2,5)
			d = rd.randint(3,8)
			self.virus.append(GenVirus(virus_colors[v], t, m, d))
		self.virus_count = len(self.virus)
		for h in range(self.hw[0]):
			l = []
			for w in range(self.hw[1]):
				l.append(GenPixel(w,h,self.background))
			self.pixels.append(l)
		center = (self.hw[0] // 2, self.hw[1] // 2)
		radius = (self.hw[0] // 5, self.hw[1] // 5)
		angle = math.pi * 2 / self.virus_count
		rotation = rd.random() * 3
		for i in range(self.virus_count):
			x = round(center[1] + math.cos(angle * i + rotation) * radius[1])
			y = round(center[0] + math.sin(angle * i + rotation) * radius[0])
			self.pixels[y][x].infection(self.virus[i%self.virus_count], i%self.virus_count)

	#Simulating a day...
	def simulate_day(self):
		for h in range(self.hw[0]):
			for w in range(self.hw[1]):
				if self.pixels[h][w].is_infected:
					v = self.pixels[h][w].virus_id
					for i in range(-3,3):
						for j in range(-3,3):
							t = rd.random()
							if t < self.virus[v].threshold:
								self.pixels[(h+i)%self.hw[0]][(w+j)%self.hw[1]].infection(self.virus[v], v)
					self.pixels[h][w].update()
		for v in self.virus:
			v.update()
		self.age += 1
