import math
import random as rd

class GenCurve():
	"A class to work with a curve..."

	resolution = math.pi/5

	def __init__(self, x, y, angle, scale, curve):
		self.p = (x,y) #current position
		self.a = angle #current angle
		self.s = scale #scale
		self.curve = curve #description of the curve
		self.points = None #points relative to (0,0)
		self.build_points()

	def get_points(self):
		points = [self.p]
		for p in self.points:
			points.append((self.p[0] + p[0], self.p[1] + p[1]))
		return points

	def random_curve(self):
		steps = rd.randint(1,5)
		self.curve = []
		for s in range(steps):
			a = rd.random() * self.resolution
			count = rd.randint(5,30)
			self.curve.append([count, a])
		self.build_points()

	def build_points(self):
		self.points = []
		last_point = (0,0)
		angle = self.a
		self.points.append(last_point)
		for data in self.curve:
			for p in range(data[0]):
				new_point = self.new_point((last_point), angle)
				self.points.append(new_point)
				last_point = new_point
				angle += data[1]

	def new_point(self, last_point, angle):
		x = math.cos(angle) * self.s
		y = math.sin(angle) * self.s
		return (last_point[0] + x, last_point[1] + y)

	def move(self, x, y):
		self.p = (self.p[0] + x, self.p[1] + y)

	def mutation(self):
		for data in self.curve:
			data[0] += rd.randint(0,4) - 2
		self.build_points()
