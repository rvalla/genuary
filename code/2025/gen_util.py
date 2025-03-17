import math
import time as tm
import random as rd
import numpy as np
from PIL import Image as im, ImageStat as stats


class GenUtil():
	"A class to join interesting functions for genuary..."

	def __init__(self):
		self.vowels = set(['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú'])
		self.symbol_color_mapping = []
		self.symbol_color_mapping.append(['e', 's', 'i', 'c', 'm', 'g', 'v', 'h', 'j', 'ñ', 'ü'])
		self.symbol_color_mapping.append(['a', 'r', 'd', 't', 'p', 'y', 'q', 'f', 'é', 'x', 'w'])
		self.symbol_color_mapping.append(['o', 'n', 'l', 'u', 'b', 'í', 'ó', 'z', 'á', 'ú', 'k'])

	#Getting a random color based on time in rgb space...
	def get_time_color(self):
		t = tm.localtime()
		r = t.tm_sec * 2
		g = t.tm_min * 2
		b = t.tm_hour * 5
		return (r,g,b)

	#Getting a random color based on time in rgba space...
	def get_time_alpha_color(self, alpha):
		t = tm.localtime()
		r = t.tm_sec * 2
		g = t.tm_min * 2
		b = t.tm_hour * 5
		return (r,g,b, alpha)

	#Moving a color randomly in rgb color space...
	def move_color(self, color, motion):
		r = rd.randint(-motion,motion)
		g = rd.randint(-motion,motion)
		b = rd.randint(-motion,motion)
		return ((color[0]+r)%256,(color[1]+g)%256,(color[2]+b)%256)

	#A function to invert a color in rgb color space...
	def invert_color(self, color):
		return (255-color[0],255-color[1],255-color[2])

	#Moving a color randomly in rgba color space...
	def move_alpha_color(self, color, motion):
		r = rd.randint(-motion,motion)
		g = rd.randint(-motion,motion)
		b = rd.randint(-motion,motion)
		a = rd.randint(-motion,motion)
		return ((color[0]+r)%256,(color[1]+g)%256,(color[2]+b)%256,(color[3]+a)%256)

	#A function to invert a color in rgba color space...
	def invert_alpha_color(self, color):
		return (255-color[0],255-color[1], 255-color[2],255-color[3])

	#Changing a color with control...
	def color_grading(self, color, destiny, speed):
		r = color[0] + round((destiny[0] - color[0]) * speed)
		g = color[1] + round((destiny[0] - color[1]) * speed)
		b = color[2] + round((destiny[0] - color[2]) * speed)
		return (r,g,b)

	#Get a color tuple from a list...
	def get_color_tuple(self, color):
		return (color[0], color[1], color[2])

	#Controlled average the colors of a matrix...
	def control_color_average_matrix(self, color_matrix, control_matrix):
		for r in range(len(color_matrix)):
			for c in range(len(color_matrix[0])):
				self.control_color_average(color_matrix[r][c], control_matrix[r][c])

	#Controlled average for color...
	def control_color_average(self, color, control):
		for i in range(3):
			if control[i] > 0:
				color[i] = color[i] // control[i]
	
	#Scaling down the colors of a matrix...
	def scale_color_matrix(self, matrix, divisor):
		for r in range(len(matrix)):
			for c in range(len(matrix[0])):
				self.scale_color(matrix[r][c], divisor)

	#Scaling down integers to fit rgb channels...
	def scale_color(self, color, divisor):
		color[0] = color[0] // divisor
		color[1] = color[1] // divisor
		color[2] = color[2] // divisor

	#Truncating the colors of a matrix...
	def truncate_color_matrix(self, matrix):
		for r in range(len(matrix)):
			for c in range(len(matrix[0])):
				self.truncate_color(matrix[r][c])

	#Truncating a color...
	def truncate_color(self, color):
		color[0] = color[0]%256
		color[1] = color[1]%256
		color[2] = color[2]%256

	#Deciding if a symbol is a vowel...
	def is_vowel(self, symbol):
		i = 1
		if symbol in self.vowels:
			i = 0
		return i
	
	#A function to map a symbol to a color rgb channel...
	def symbol_to_color_data(self, symbol):
		c = None
		v = None
		if symbol in self.symbol_color_mapping[0]:
			c = 0
			v = 255 - (21 * (self.symbol_color_mapping[0].index(symbol) + 1))
		elif symbol in self.symbol_color_mapping[1]:
			c = 1
			v = 255 - (21 * (self.symbol_color_mapping[1].index(symbol) + 1))
		elif symbol in self.symbol_color_mapping[2]:
			c = 2
			v = 255 - (21 * (self.symbol_color_mapping[2].index(symbol) + 1))
		else:
			c = rd.choice([0,1,2])
			v = 5
		return c, v

	#A function to get color matrix from an image...
	def get_image_data(self, image_path, height, width):
		image = im.open(image_path).resize((width, height))
		return np.array(image)

	#A function to get an image combining two images...
	def mean_image(self, back_image, top_image, name):
		back_image.convert("RGBA")
		top_image.convert("RGBA").resize(back_image.size)
		mask = im.new("L", back_image.size, 127)
		new = im.composite(back_image, top_image, mask)
		new.save(name + ".jpg")

	#A function to paint a mask with an input image...
	def mask_merge(self, background, top_image, name):
		top_image.convert("RGBA")
		mask = im.open(self.mask_path + rd.choice(self.input_mask_list)).convert("L").resize(top_image.size)
		back_image = im.new("RGBA", top_image.size, background)
		new = im.composite(back_image, top_image, mask)
		new.save(name + ".jpg")
	
	#A function to save a framed image...
	def save_frame_image(self, top_image, margins, name):
		frame = im.new("RGB", (top_image.size[0] + margins[1] * 2, top_image.size[1] + margins[0] * 2), (255,255,255))
		frame.paste(top_image, (margins[1], margins[0]))
		frame.save(name + ".jpg")

	#A function to build a random signal...
	def random_signal(self, base_frequency, base_amplitude, components):
		signal = []
		for c in range(components):
			fq = rd.random() * base_frequency
			a = base_amplitude / (c + 1)
			fase = rd.random() * math.pi * 2
			signal.append((fq, a, fase))
		return signal

	#A function to build a harmonic signal...
	def harmonic_signal(self, base_frequency, base_amplitude, components):
		signal = []
		for c in range(components):
			fq = base_frequency * (c + 1)
			a = base_amplitude / (c + 1)
			fase = rd.random() * math.pi * 2
			signal.append((fq, a, fase))
		return signal
	
	#A function to get signal amplitude...
	def get_signal_y(self, signal, angle, scale):
		y = 0
		for s in signal:
			y += math.sin(s[0] * angle + s[2]) * s[1] * scale
		return y

	def gen_alpha_rectangle(self, canvas, w, h, location, density, colors, color_motion, factors, size_factor, constant_size):
		steps = [h // density[0], w // density[1]]
		thinghw = [steps[1] * size_factor, steps[0] * size_factor]
		color_count = len(colors)
		active_color = rd.randint(0,color_count-1)
		aux_size = thinghw
		for i in range(density[0]):
			active_color = (active_color+i)%color_count
			c = colors[active_color]
			if not constant_size:
				aux_size = (aux_size[0] , (thinghw[1] + i%(4*steps[1])))
			for j in range(density[1]):
				x = location[1] + steps[1] / 2 + (j * factors[0])%density[1] * steps[1]
				y = location[0] + steps[0] / 2 + (j * factors[1] + i * factors[0])%density[0] * steps[0]
				center = (x, y)
				if not constant_size:
					aux_size = (thinghw[0] + j%(4*steps[0]), aux_size[1])
				canvas.draw_rectangle(c, center, aux_size)
				c = self.move_alpha_color(c, color_motion)
			colors[active_color] = c

	def gen_rectangle(self, canvas, w, h, location, density, colors, color_motion, factors, size_factor, constant_size):
		steps = [h // density[0], w // density[1]]
		thinghw = [steps[1] * size_factor, steps[0] * size_factor]
		color_count = len(colors)
		active_color = rd.randint(0,color_count-1)
		aux_size = thinghw
		for i in range(density[0]):
			active_color = (active_color+i)%color_count
			c = colors[active_color]
			if not constant_size:
				aux_size = (aux_size[0] , (thinghw[1] + i%(4*steps[1])))
			for j in range(density[1]):
				x = location[1] + steps[1] / 2 + (j * factors[0])%density[1] * steps[1]
				y = location[0] + steps[0] / 2 + (j * factors[1] + i * factors[0])%density[0] * steps[0]
				center = (x, y)
				if not constant_size:
					aux_size = (thinghw[0] + j%(4*steps[0]), aux_size[1])
				canvas.draw_rectangle(c, center, aux_size)
				c = self.move_color(c, color_motion)
			colors[active_color] = c
	
	def gen_sampled_rectangle(self, canvas, w, h, location, density, image, size_factor):
		steps = [h // density[0], w // density[1]]
		thinghw = [steps[1] * size_factor, steps[0] * size_factor]
		aux_size = thinghw
		for i in range(density[0]):
			for j in range(density[1]):
				x = steps[1] / 2 + j * steps[1]
				y = steps[0] / 2 + (j + i)%density[0] * steps[0]
				c = (image[int(y)][int(x)][0], image[int(y)][int(x)][1], image[int(y)][int(x)][2]) 
				center = (location[1] + x, location[0] + y)
				canvas.draw_rectangle(c, center, aux_size)
