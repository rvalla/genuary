import gen
from gen_util import GenUtil
import random as rd

ut = GenUtil()

#Genuary29 (Grid-based graphic design)
#gen_29((h,w),(mh,mw),background,grid_size,text,name)
gen.gen_29((1080,1080), (100,100), (255,255,255), 16, "There is a text here", "name")
