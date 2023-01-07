import gen
from gen_util import GenUtil
import random as rd

ut = GenUtil()

#Genuary1 (creating frames for a loop - I use ImageMagick to make the gif)
#gen_1((h,w),(mh,mw),background,signal,color,signal_height,rounds,angle_unit,name)
gen.gen_1((880,1720), (100,100), (255,255,255), ut.harmonic_signal(1,1,5), (160,125,56), 150, 10, 0.05, "1")

#Genuary2 (creating something in 10 minutes)
#gen_2((h,w),(mh,mw),background,color,noise_width,lines,lines_width,name)
gen.gen_2((760,1600), (160,160), (255,255,255), (10,150,190), 100, 1600, 1, "1")

#Genuary3 (creating something inspired by glitch art)
#gen_3(hw, mg, background, image_path, row_offset, column_offset, offset_threshold, name)
gen.gen_3((800,1200), (140,360), (0,0,0), "assets/input/gen3_02.jpg", 240, 240, 0.5, "10")