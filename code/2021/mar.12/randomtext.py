import json as js
import random as rd

class RandomText():
	"Generating text randomly"

	def __init__(self, configpath, fpath):
		self.config = js.load(open(configpath))
		self.letters, self.frequency = self.load_letter_frequency(fpath)
		self.words_size = [float(i) for i in self.config["wordsSize"].split(",")]
		self.line_width = self.config["lineWidth"]
		self.out_path = self.config["outPath"]
		self.out_file = self.config["outFile"]
		self.iterations = self.config["iterations"]
		self.m = ""

	def speak(self, w_count):
		self.m = ""
		for i in range(1, w_count + 1):
			self.m += self.build_word()
			if i % self.line_width == 0:
				self.m += "\n"
			else:
				self.m += " "
		return self.m

	def save_to_file(self):
		file = open(self.out_path + self.out_file + ".txt", "w")
		file.write(self.m)
		file.close()

	def build_word(self):
		w = ""
		s = self.decide_word_size()
		for i in range(s):
			w += self.decide_letter()
		return w

	def decide_letter(self):
		r = rd.random()
		p = 0
		while r > self.frequency[p]:
			p += 1
		return self.letters[p]

	def decide_word_size(self):
		return round(rd.triangular(self.words_size[0],self.words_size[2],self.words_size[1]))

	def load_letter_frequency(self, fpath):
		data = js.load(open(fpath))
		s_letters = data[self.config["letters"]]
		s_frequency = data[self.config["frequency"]]
		letters = s_letters.split(",")
		aux_frequency = [float(i) for i in s_frequency.split(",")]
		cumulative_p = 0
		frequency = []
		for i in range(len(aux_frequency)-1):
			cumulative_p += aux_frequency[i]
			frequency.append(cumulative_p)
		frequency.append(1.0)
		return letters, frequency

	def __str__(self):
		return "-- randomtext --\n" + \
				"-- https://gitlab.com/rodrigovalla/genuary2021\n" + \
				"-- version: 0.50\n"
