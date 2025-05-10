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

#Genuary4 (creating something with intersections)
#gen_4(hw, mg, background, signal_a, signal_b, signal_height, angle_unit, colors, color_motion, name)
signal_a = ut.harmonic_signal(1,1,4) #A random signal to draw a curve
signal_b = ut.random_signal(1,1,4) #Another signal
colors = [(120,50,0),(50,120,0),(0,50,120)] #The colors
gen.gen_4((880,1720), (100,100), (255,255,255), signal_a, signal_b, 150, 0.005, colors, 45, "12")

#Genuary6 
#gen_6(hw, mg, background, image_path, rounds, name)
gen.gen_6((800,800), (140,560), (255,255,255), "assets/input/gen6_01.jpg", 10, "4")

#Genuary7 (creating something with the colors from an album cover)
#gen_7(hw, mg, background, image_path, density, size_factor, rounds, name)
gen.gen_7((800,800), (140,560), (255,255,255), "assets/input/gen7_01.jpg", [9,9], 0.8, 4, "1")

#Genuary23 (more moiré)
signal = ut.random_signal(1,1,6)
gen.gen_23((1080,1920), (140,140), (255,255,255), (75,50,25), 30, signal, 30, 0.02, 0.45, 0.35, "23")
