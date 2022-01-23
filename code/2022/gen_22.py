import math
import datetime as dt
import random as rd
from gen_curve import GenCurve
from gen_color import GenColor
from gen_util import GenUtil
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen22():
	"The class to create something that will look completely different in a year..."

	def __init__(self, active_width, active_height, background, color_motion, step_size, base_angle, variation,
					scale, line_w, date):
		self.zero_date = dt.datetime(2022,1,22)
		self.date, self.years, self.days = self.get_date_data(date)
		self.background = background
		self.hw = [active_height, active_width]
		self.canvas = DCanvas(self.hw[1], self.hw[0], background)
		self.color = GenColor(ut.get_time_color())
		self.lw = line_w
		self.step_size = step_size
		self.curve = GenCurve(self.hw[1] // 2, self.hw[0] // 4, 0, scale, self.curve_description(step_size, base_angle, variation))
		self.draw_curve(color_motion)

	def draw_curve(self, color_motion):
		points = self.curve.get_points()
		for d in range(365):
			for s in range(self.step_size):
				self.canvas.draw_line(self.color.c, self.lw, points[d*self.step_size+s], points[d*self.step_size+s+1])
			self.color.translate(color_motion)

	def curve_description(self, step_size, base_angle, variation):
		data = [[step_size, base_angle] for d in range(365)] #The curve has 365 segments...
		for s in range(self.days):
			data[s][1] += rd.random() * variation * self.years
		return data

	#Checking which day of the cycle is today...
	def get_date_data(self, input):
		date = None
		if input == None:
			date = dt.date.today()
		else:
			date = dt.datetime(input[0],input[1],input[2])
		years = date.year - self.zero_date.year + 1
		days = ((date - self.zero_date).days)%365
		return date, years, days
