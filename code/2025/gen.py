import random as rd
from gen_util import GenUtil
from gen_color import GenColor
from gen_drawing_canvas import DCanvas
from gen_data_canvas import NCanvas

ut = GenUtil()

def gen_29(hw, mg, background, grid_size, text, name):
	"The function to create a beautiful grid..."

	canvas = DCanvas(hw[1] + mg[1] * 2, hw[0] + mg[0] * 2, background)
	sq_size = hw[0]//grid_size
	c_size = round(sq_size * 0.6)
	if len(text)%2 == 1:
		text = text + " "
	text_center = len(text)//2
	row_matrix = [[[255,255,255] for i in range(grid_size)] for i in range(grid_size)]
	col_matrix = [[[255,255,255] for i in range(grid_size)] for i in range(grid_size)]

	#We use the first half of the text to decide vertical pattern...
	for i in range(text_center):
		ch, v = ut.symbol_to_color_data(text[i])
		is_v = ut.is_vowel(text[i])
		for r in range(grid_size//2):
			row_matrix[i%grid_size][2*r+is_v][ch] += v

	#We use the second half of the text to decide horizontal pattern...
	for i in range(text_center):
		ch, v = ut.symbol_to_color_data(text[text_center+i])
		is_v = ut.is_vowel(text[text_center+i])
		for c in range(grid_size//2):
			col_matrix[2*c+is_v][i%grid_size][ch] += v

	#Estimation to scale colors
	ut.truncate_color_matrix(row_matrix)
	ut.truncate_color_matrix(col_matrix)

	x_offset = mg[0] + sq_size//2
	y_offset = mg[1] + sq_size//2 
	for r in range(grid_size):
		for c in range(grid_size):
			canvas.draw_rectangle(ut.get_color_tuple(row_matrix[r][c]), (r*sq_size+x_offset, c*sq_size+y_offset), (sq_size, sq_size))
			canvas.draw_circle(ut.get_color_tuple(col_matrix[r][c]), (r*sq_size+x_offset, c*sq_size+y_offset), c_size)

	canvas.save("assets/img/", "gen29_" + name)
