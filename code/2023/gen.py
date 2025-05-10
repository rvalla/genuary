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

def gen_6(hw, mg, background, image_path, rounds, name):
	"The function to make something stealing like an artist..."

	canvas = DCanvas(hw[1] + mg[1] * 2, hw[0] + mg[0] * 2, background)
	image = ut.get_image_data(image_path, hw[0], hw[1])

	for r in range(1,rounds):
		w = hw[1] // pow(2,r)
		h = hw[0] // pow(2,r)
		for t in range(rd.randint(1,pow(2,r) + 1)):
			x = rd.randint(0,pow(2,r)-1) * w + w // 2
			y = rd.randint(0,pow(2,r)-1) * h + + h // 2
			location = (mg[1] + x, mg[0] + y)
			c = (image[int(y)][int(x)][0], image[int(y)][int(x)][1], image[int(y)][int(x)][2])
			canvas.draw_circle(c, location, w)

	canvas.save("assets/img/", "gen6_" + name)

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

def gen_23(hw, mg, background, color, color_motion, signal, signal_height, angle_unit, fase_offset_w, mutation_width, name):
	"Let's create a moiré pattern..."

	canvas = DCanvas(hw[1] + mg[1] * 2, hw[0] + mg[0] * 2, background)
	i_color = ut.invert_color(color)

	for r in range(1,hw[0]//5):
		start_angle = rd.random()*fase_offset_w
		last_y = ut.get_signal_y(signal, angle_unit + start_angle, signal_height)
		last_x = last_y
		for c in range(1,hw[1]):
			y = ut.get_signal_y(signal, start_angle + (angle_unit * c), signal_height)
			canvas.draw_line(color,1,(mg[0]+c, mg[1]+r*5+last_y), (mg[0]+c, mg[1]+r*5+y))
			last_y = y
		ut.mutate_signal(signal, mutation_width)
		color = ut.move_color(color, color_motion)
	for c in range(1,hw[1]//5):
		for r in range(1,hw[0]):
			x = ut.get_signal_y(signal, start_angle + (angle_unit * r), signal_height)
			canvas.draw_line(i_color,1,(mg[0]+c*5+last_x, mg[1]+r), (mg[0]+c*5+x, mg[1]+r))
			last_x = x
		ut.mutate_signal(signal, mutation_width)
		i_color = ut.move_color(i_color, color_motion)

	canvas.save("assets/img/", "gen23_" + name)
