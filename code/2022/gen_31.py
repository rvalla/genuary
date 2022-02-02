import math
import random as rd
import numpy as np
from PIL import Image as im
from gen_pixel import GenPixel
from gen_virus import GenVirus
from gen_util import GenUtil
from gen_data_canvas import NCanvas

ut = GenUtil()

class Gen31():
	"The class to create something with negative space..."

	def __init__(self, active_width, active_height, margins, base_image, virus_thresholds, contacts_width, days):
		self.margins = margins
		self.hw = [active_height, active_width]
		self.canvas = NCanvas(self.hw[1] + self.margins[1] * 2, self.hw[0] + self.margins[0] * 2, (0,0,0))
		self.canvas.load_data(base_image)
		self.age = 0
		self.days = days
		self.virus_thresholds = virus_thresholds
		self.virus = None
		self.pixels = []
		self.simulate(contacts_width)
		self.paint_result()

	#Simulating an epidemic...
	def simulate(self, contacts_width):
		self.start_epidemic(contacts_width)
		print("Ready to simulate the epidemic...", end="\n")
		while self.age < self.days:
			print("Simulating day " + str(self.age), end="\r")
			self.simulate_day()

	#Painting the result...
	def paint_result(self):
		print("Painting result...            ", end="\r")
		for h in range(self.hw[0]):
			for w in range(self.hw[1]):
				self.canvas.paint_pixel(self.pixels[h][w].c, w + self.margins[1], h + self.margins[0])
		print("Result is ready...", end="\n")

	#Starting the epidemic...
	def start_epidemic(self, contacts_width):
		t = rd.uniform(self.virus_thresholds[0],self.virus_thresholds[1])
		m = rd.randint(121,134)
		d = rd.randint(2,3)
		self.virus = GenVirus((0,0,0), contacts_width, t, m, d)
		for h in range(self.hw[0]):
			l = []
			for w in range(self.hw[1]):
				l.append(GenPixel(w,h,self.canvas.data[h + self.margins[0]][w + self.margins[1]]))
			self.pixels.append(l)
		center = (self.hw[0] // 2, self.hw[1] // 2)
		self.pixels[center[0]][center[1]].infection(self.virus, 0, self.canvas.get_inverted_pixel_color(center[1],center[0]))

	#Simulating a day...
	def simulate_day(self):
		infected_pixels = self.infected_list()
		for p in infected_pixels:
			limits = self.virus.contacts
			for i in range(limits[0],limits[1]):
				for j in range(limits[0],limits[1]):
					t = rd.random()
					if t < self.virus.threshold:
						x = p[1] + j
						y = p[0] + i
						if y >= 0 and y < self.hw[0] and x >= 0 and x < self.hw[1]:
							self.pixels[y][x].infection(self.virus, 0, self.canvas.get_inverted_pixel_color(x+self.margins[1],y+self.margins[0]))
							a = 1
			self.pixels[p[0]][p[1]].update()
		self.virus.update()
		self.age += 1

	#Building infected pixels list...
	def infected_list(self):
		l = []
		for h in range(self.hw[0]):
			for w in range(self.hw[1]):
				if self.pixels[h][w].is_infected:
					l.append((h,w))
		return l
