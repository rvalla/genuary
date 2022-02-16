import math

class GenMessageCurve():
	"A class to transform text into curves..."

	#Building the curve...
	def __init__(self, message, width, height, margins):
		self.s = [width, height]
		self.m = margins
		self.length = len(message) + 1
		self.limits = [[0,0.01],[0,0.01]]
		self.points = [(0,0)]
		self.blanks = set()
		self.subdivisions = [3,4,5,6,8,12,16]
		self.module = self.subdivisions[len(message)%7]
		self.base_angle = math.pi * 2 / self.module
		self.build_points(message)
		self.scales, self.margins = self.get_scales_and_margins()

	#Returning an specific point adjusting it to the canvas...
	def get_point(self, position):
		x = (self.points[position][0] - self.limits[0][0]) * self.scales[0] + self.margins[0]
		y = (self.points[position][1] - self.limits[1][0]) * self.scales[1] + self.margins[1]
		return (x,y)

	#Returning the color for an specific segment...
	def get_color(self, position):
		if position in self.blanks:
			return 1
		else:
			return 0

	#Building the curve of scale 1...
	def build_points(self, message):
		last_point = (0,0)
		angle = 0
		for l in range(len(message)):
			o = ord(message[l])
			n = (o-32)%self.module
			angle += self.base_angle * (n + 1)
			p = self.get_new_point(last_point, angle)
			self.points.append(p)
			self.update_limits(p)
			last_point = p
			if o == 32 or o == 9 or o == 10:
				self.blanks.add(l + 1)

	#A new point...
	def get_new_point(self, last_point, angle):
		x = math.cos(angle)
		y = math.sin(angle)
		return (last_point[0] + x, last_point[1] + y)

	#Storing minimun and maximun width and height...
	def update_limits(self, point):
		if point[0] < self.limits[0][0]:
			self.limits[0][0] = point[0]
		elif point[0] > self.limits[0][1]:
			self.limits[0][1] = point[0]
		if point[1] < self.limits[1][0]:
			self.limits[1][0] = point[1]
		elif point[1] > self.limits[1][1]:
			self.limits[1][1] = point[1]

	#Finishing the creation of the curve...
	def get_scales_and_margins(self):
		w = abs(self.limits[0][0] - self.limits[0][1])
		h = abs(self.limits[1][0] - self.limits[1][1])
		scales = [self.s[0] / w]
		scales.append(self.s[1] / h)
		margins = None
		if scales[0]*w < scales[1]*h:
			margins = [(self.s[0]-scales[0]*w)/2+self.m[1],self.m[0]]
		else:
			margins = [self.m[1],(self.s[1]-scales[1]*h)/2+self.m[0]]
		return scales, margins
