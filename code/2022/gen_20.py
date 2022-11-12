import random as rd
from gen_util import GenUtil
from gen_curve import GenCurve
from gen_drawing_canvas import DCanvas

ut = GenUtil()

class Gen20():
	"The class to make a sea of shapes..."

	def __init__(self, active_width, active_height, background, color, color_motion, curve):
		self.hw = (active_height, active_width)
		self.color = color
		self.curve = curve
		self.canvas = DCanvas(self.hw[1], self.hw[0], background)
		self.paint(color_motion)

	def paint(self, color_motion):
		for i in range(7):
			self.draw_curve(color_motion)
			self.color = ut.move_color(self.color, color_motion)
			self.curve.move(0,self.hw[0]//20)

	def draw_curve(self, color_motion):
		for p in self.curve.get_points():
			self.canvas.draw_circle(self.color, p, rd.randint(20,50))
