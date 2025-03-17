import math
import random as rd
from gen_util import GenUtil
from gen_color import GenColor
from gen_drawing_canvas import DCanvas
from gen_data_canvas import NCanvas

ut = GenUtil()

def gen_29(sq_size, mg, symbols_per_row_and_column, background, text, name):
	"The function to create a beautiful grid based on text..."

	#We are going to assign n symbols to each row and column...
	sym_count = symbols_per_row_and_column
	
	#Then we make sure that text length is divisible by 2 * sym_count...
	if not len(text)%(2*sym_count) == 0:
		for i in range(2*sym_count-len(text)%(2*sym_count)):
			text += " "

	#Now we need some variables...
	text_center = len(text)//2 #Half of the text for rows, half for columns...
	grid_size = len(text)//(2*sym_count)
	if grid_size%2 == 1: #We need an even grid_size
		grid_size -= 1
	c_size = round(min(sq_size[0], sq_size[1]) * 0.6)

	#Here we have two matrices to save the color of cells and two matrices to control future average calculation...
	row_matrix = [[[background[0],background[1],background[2]] for i in range(grid_size)] for i in range(grid_size)]
	row_control = [[[1,1,1] for i in range(grid_size)] for i in range(grid_size)]
	col_matrix = [[[background[0],background[1],background[2]] for i in range(grid_size)] for i in range(grid_size)]
	col_control = [[[1,1,1] for i in range(grid_size)] for i in range(grid_size)]
	
	#We use the first half of the text to decide vertical pattern...
	for i in range(text_center):
		ch, v = ut.symbol_to_color_data(text[i])
		is_v = ut.is_vowel(text[i])
		for r in range(grid_size//2):
			row_matrix[i%grid_size][2*r+is_v][ch] += v
			row_control[i%grid_size][2*r+is_v][ch] += 1

	#We use the second half of the text to decide horizontal pattern...
	for i in range(text_center):
		ch, v = ut.symbol_to_color_data(text[text_center+i])
		is_v = ut.is_vowel(text[text_center+i])
		for c in range(grid_size//2):
			col_matrix[2*c+is_v][i%grid_size][ch] += v
			col_control[2*c+is_v][i%grid_size][ch] += 1
	
	#Now we calculate average value for each color channel in each cell...
	ut.control_color_average_matrix(row_matrix, row_control)
	ut.control_color_average_matrix(col_matrix, col_control)

	#We need a canvas now...
	canvas = DCanvas(sq_size[1] * grid_size + mg[1] * 2, sq_size[0] * grid_size + mg[0] * 2, background)

	#We are ready to draw our canvas...
	x_offset = mg[0] + sq_size[0]//2
	y_offset = mg[1] + sq_size[1]//2 
	for r in range(grid_size):
		for c in range(grid_size):
			canvas.draw_rectangle(ut.get_color_tuple(row_matrix[r][c]), (r*sq_size[1]+y_offset, c*sq_size[0]+x_offset), (sq_size[1], sq_size[0]))
			canvas.draw_circle(ut.get_color_tuple(col_matrix[r][c]), (r*sq_size[1]+y_offset, c*sq_size[0]+x_offset), c_size)
	
	canvas.show()
	#canvas.save("assets/img/", "gen29_" + name)
