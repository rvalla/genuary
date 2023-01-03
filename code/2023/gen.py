import random as rd
from gen_util import GenUtil
from gen_color import GenColor
from gen_drawing_canvas import DCanvas
from gen_data_canvas import NCanvas

ut = GenUtil()

def gen_1(hw, margins, background, signal, color, signal_height, rounds, angle_unit, name):
	"The function to create some material for a loop..."

	canvas = DCanvas(hw[1] + margins[1] * 2, hw[0] + margins[0] * 2, background)
	color = GenColor(color)
	zero = hw[0] // 2

	for r in range(rounds):
		for l in range(hw[1]):
			y = zero + ut.get_signal_y(signal, r*hw[1] + l * angle_unit, signal_height)
			canvas.draw_line(color.c, 1, (margins[1] + l%hw[1], y), (margins[1]+l%hw[1], hw[0]))
		color.move(60)
		canvas.save("assets/img/", "gen1_" + name + "_" + str(r))
	

