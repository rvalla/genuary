from gen_util import GenUtil
from gen_drawing_canvas import DCanvas
from gen_message_curve import GenMessageCurve

ut = GenUtil()

class Gen19B():
	"The class to create something with text..."

	def __init__(self, active_width, active_height, margins, background, color, color_motion, line_width, message, module):
		self.hw = [active_height, active_width]
		self.lw = line_width
		self.margins = margins
		self.canvas = DCanvas(self.hw[1] + self.margins[1] * 2, self.hw[0] + self.margins[0] * 2, background)
		self.curve = GenMessageCurve(message, module, active_width, active_height, margins)
		self.colors = [color, ut.invert_color(color)]
		self.paint_curve(color_motion)

	def paint_curve(self, color_motion):
		last_point = self.curve.get_point(0)
		for p in range(1,self.curve.length):
			point = self.curve.get_point(p)
			c = self.curve.get_color(p)
			self.canvas.draw_line(self.colors[c], self.lw, point, last_point)
			last_point = point
			if c == 1:
				self.colors[0] = ut.move_color(self.colors[0], color_motion)
				self.colors[1] = ut.move_color(self.colors[1], color_motion)
