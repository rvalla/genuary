import gen
from gen_util import GenUtil
import random as rd

ut = GenUtil()

#Genuary29 (Grid-based graphic design)
#We load some text first
text = open("assets/input/borges_remordimiento.txt").read()
#gen_29((sq_size_h,sq_size_w),(mh,mw), symbols_per_row_and_column, background, text, name)
gen.gen_29((45,45), (100,100), 8, (255,255,255), text, "name")
#gen_29((sq_size_h,sq_size_w),(mh,mw), grid_size, background, text, name)
gen.gen_29b((45,45), (100,100), 8, (255,255,255), text, "name")
#gen_29((sq_size_h,sq_size_w),(mh,mw), grid_size, background, text, name)
gen.gen_29c((45,45), (100,100), 8, (255,255,255), text, "name")
