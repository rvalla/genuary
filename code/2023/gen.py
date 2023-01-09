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

def gen_3(hw, mg, background, image_path, row_offset, column_offset, offset_threshold, name):
	"The function to create some glitch art..."

	canvas = NCanvas(hw[1], hw[0], background)
	canvas.load_data(image_path)
	image = ut.get_image_data(image_path, hw[0], hw[1])

	for r in range(hw[0]):
		if rd.random() < offset_threshold:
			canvas.paint_row(image[r], r, rd.randint(0,row_offset))
	
	for c in range(hw[1]):
		if rd.random() < offset_threshold:
			canvas.paint_column(image[:,c], c, rd.randint(0,column_offset))
	
	file_name = "assets/img/gen3_" + name
	ut.save_frame_image(canvas.get_image(), mg, file_name)

def gen_4(hw, mg, background, signal_a, signal_b, signal_height, angle_unit, colors, color_motion, name):
	"The function to draw the intersection between two signals..."

	canvas = DCanvas(hw[1] + mg[1] * 2, hw[0] + mg[0] * 2, background)
	colors = [GenColor(c) for c in colors]
	active_color = 0
	zero = hw[0] // 2
	signal_a = [round(ut.get_signal_y(signal_a, x * angle_unit, signal_height),2) for x in range(hw[1])]
	signal_b = [round(ut.get_signal_y(signal_b, x * angle_unit, signal_height),2) for x in range(hw[1])]

	for c in range(hw[1]):
		x = mg[1] + c
		y1 = zero + signal_a[c]
		y2 = zero + signal_b[c]
		canvas.draw_line(colors[active_color].c, 1, (x, mg[0] + y1), (x, mg[0] + y2))

		if abs(y1 - y2) < 2:
			colors[active_color].move(color_motion)
			active_color = (active_color + 1) % len(colors)

	canvas.save("assets/img/", "gen4_" + name)

def gen_7(hw, mg, background, image_path, density, size_factor, rounds, name):
	"The function to make something sampling colors..."

	canvas = DCanvas(hw[1] + mg[1] * 2, hw[0] + mg[0] * 2, background)
	
	for r in range(rounds):
		w = hw[1] // pow(2,r)
		h = hw[0] // pow(2,r)
		image = ut.get_image_data(image_path, h, w)
		for t in range(rd.randint(1,pow(2,r) + 1)):
			location = (mg[0] + rd.randint(0,pow(2,r)-1) * w, mg[1] + rd.randint(0,pow(2,r)-1) * h)
			ut.gen_sampled_rectangle(canvas, w, h, location, density, image, size_factor)

	canvas.save("assets/img/", "gen7_" + name)