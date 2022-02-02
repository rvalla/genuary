class GenPixel():
	"A class to work with an interesting pixel..."

	def __init__(self, x, y, color):
		self.virus_id = None
		self.x = x
		self.y = y
		self.c = color
		self.is_infected = False
		self.is_immune = False
		self.infection_evol = None
		self.infection_end = None

	def infection(self, virus, virus_id, color):
		if self.is_infected == False and self.is_immune == False:
			self.infection_evol = 0
			self.c = color
			self.virus_id = virus_id
			self.is_infected = True
			self.infection_end = virus.duration

	def update(self):
		self.infection_evol += 1
		if self.infection_evol > self.infection_end:
			self.is_infected = False
			self.is_immune = True
