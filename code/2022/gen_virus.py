import random as rd
from gen_util import GenUtil

ut = GenUtil()

class GenVirus():
	"A class to infect pixels..."

	def __init__(self, color, contacts_width, threshold, mutation_cycle, duration):
		self.color = color
		self.negative_color = ut.invert_color(self.color)
		self.contacts_width = contacts_width
		self.contacts = None
		self.set_contacts(contacts_width)
		self.threshold = threshold
		self.mutation_cycle = mutation_cycle
		self.last_mutation = 0
		self.age = 0
		self.duration = duration

	def set_contacts(self, contacts_width):
		c = rd.randint(0,contacts_width)
		self.contacts = (c - self.contacts_width, c)

	def update(self):
		self.age += 1
		if self.age - self.last_mutation > self.mutation_cycle:
			self.threshold = self.threshold + (rd.random() - 0.3) / 120
			self.color = ut.move_color(self.color, 10)
			self.last_mutation = self.age
			self.set_contacts(self.contacts_width)
