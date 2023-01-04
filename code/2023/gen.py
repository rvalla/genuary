import random as rd
from gen_util import GenUtil
from gen_color import GenColor
from gen_drawing_canvas import DCanvas
from gen_data_canvas import NCanvas

ut = GenUtil()

def gen_1(hw, mg, background, signal, color, signal_height, rounds, angle_unit, name):
	"The function to create some material for a loop..."

	canvas = DCanvas(hw[1] + mg[1] * 2, hw[0] + mg[0] * 2, background)
	color = GenColor(color)
	zero = hw[0] // 2

	for r in range(rounds):
		for l in range(hw[1]):
			y = zero + ut.get_signal_y(signal, r*hw[1] + l * angle_unit, signal_height)
			canvas.draw_line(color.c, 1, (mg[1] + l%hw[1], y), (mg[1]+l%hw[1], hw[0]))
		color.move(60)
		canvas.save("assets/img/", "gen1_" + name + "_" + str(r))
	

def gen_2(hw, mg, background, color, noise_width, lines, lines_width, name):
	"The function to try to create something in 10 minutes..."

	canvas = DCanvas(hw[1] + mg[1] * 2, hw[0] + mg[0] * 2, background)
	color = GenColor(color)
	step = hw[1] // lines

	for l in range(lines):
		n = rd.random() * noise_width - noise_width / 2
		if l % 2 == 0:
			canvas.draw_line(color.c, lines_width, (mg[1] + l * step + n, mg[0]), (mg[1]+ l * step, hw[0] + mg[0]))
		else:
			canvas.draw_line(color.c, lines_width, (mg[1] + l * step, mg[0]), (mg[1]+ l * step + n, hw[0] + mg[0]))
		color.move(3)
	
	canvas.save("assets/img/", "gen2_" + name)