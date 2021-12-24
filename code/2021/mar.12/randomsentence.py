import json as js
import random as rd

class RandomSentence():
	"Generating sentences randomly"

	def __init__(self, configpath):
		self.config = js.load(open(configpath))
		self.sentence_size = [float(i) for i in self.config["sentenceSize"].split(",")]
		self.out_path = self.config["outPath"]
		self.in_path = self.config["inPath"]
		self.in_lines = self.load_in_lines(self.in_path + self.config["inFile"])
		self.line_count = len(self.in_lines)
		self.out_file = self.config["outFile"]
		self.iterations = self.config["iterations"]
		self.m = ""

	def speak(self, s_count):
		for i in range(s_count):
			self.m += self.build_sentence()
		return self.m

	def build_sentence(self):
		size = self.decide_sentence_size()
		s = ""
		s += self.choose_word("start")
		for w in range(size - 2):
			s += self.choose_word("middle")
		s += self.choose_word("end")
		return s

	def choose_word(self, position):
		s = []
		while len(s) < 3:
			l = rd.randint(0, self.line_count - 1)
			s = self.in_lines[l].split(" ")
		if position == "start":
			return s[0] + " "
		elif position == "middle":
			w = rd.randint(1, len(s) - 2)
			return s[w] + " "
		elif position == "end":
			return s[len(s)-1]

	def save_to_file(self):
		file = open(self.out_path + self.out_file + ".txt", "w")
		file.write(self.m)
		file.close()

	def load_in_lines(self, file):
		f = open(file, "r")
		return f.readlines()

	def decide_sentence_size(self):
		return round(rd.triangular(self.sentence_size[0],self.sentence_size[2],self.sentence_size[1]))

	def __str__(self):
		return "-- randomtext --\n" + \
				"-- https://gitlab.com/rodrigovalla/genuary2021\n" + \
				"-- version: 0.50\n"
