from gen_1 import Gen1
from gen_2 import Gen2
from gen_3 import Gen3
from gen_4 import Gen4
from gen_5 import Gen5
from gen_6 import Gen6
from gen_7 import Gen7
from gen_7B import Gen7B
from gen_8 import Gen8
from gen_9 import Gen9
from gen_10 import Gen10
from gen_13 import Gen13
from gen_15 import Gen15
from gen_16 import Gen16
from gen_17 import Gen17
from gen_util import GenUtil
import random as rd

ut = GenUtil()

#Gen 1
for i in range(1):
	name = "gen1_" + str(i + 1)
	colors = [(160,160,160,25),(0,0,0,25),(50,50,50,25)]
	p = Gen1(500, 500, [200,400], (255,255,255), colors, 10, [13,0], 1, False)
	p.canvas.canvas.show()

#Gen 2
for i in range(1):
	name = "gen2_" + str(i + 1)
	p = Gen2("assets/input/test.jpg", 50, [100,50], (255,255,255))
	p.canvas.show()

#Gen 3
for i in range(1):
	name = "gen3_" + str(i + 1)
	colors = [(160,160,160),(0,0,0),(50,50,50)]
	t = [0.005,0.03]
	p = Gen3(500, 500, [50,100], (255,255,255), colors, t, 7, 30)
	p.canvas.show()

#Gen 4
for i in range(1):
	name = "gen4_" + str(i + 1)
	colors = [(160,160,160),(0,0,0),(50,50,50)]
	angle_var = [i*3.9,i*-0.3]
	p = Gen4(600,600,[90,60],(255,255,255),colors,0,[300,300],1,8,angle_var,200,False)
	p.canvas.canvas.show()

#Gen 5
for i in range(1):
	name = "gen5_" + str(i + 1)
	colors = [(160,60,160,25),(0,0,0,25),(50,160,50,25)]
	p = Gen5(660, 660, [210,630], (255,255,255), colors, 10, [13,0], 1, False, 500, 3)
	p.canvas.canvas.show()

#Gen 6
for i in range(1):
	name = "gen6_" + str(i + 1)
	color = (100,100,100)
	signal_A = ut.random_signal(3,15,5)
	signal_B = ut.random_signal(-4,15,4)
	p = Gen6(800, 800, [100,100], (0,0,0), color, signal_A, signal_B, 0.01, 120, 10, True, 0.01)
	p.canvas.canvas.show()

#Gen 7
for i in range(1):
	name = "gen7_" + str(i + 1)
	color = (240,0,100)
	p = Gen7(600, 600, [100,100], (255,255,255), color, 10, 5)
	p.canvas.canvas.show()

#Gen 7B
for i in range(1):
	name = "gen7B_" + str(i + 1)
	color = (240,0,100)
	p = Gen7B(600, 600, [100,100], (255,255,255), color, 50, 0)
	p.canvas.canvas.show()

#Gen 8
for i in range(1):
	name = "gen8_" + str(i + 1)
	color = (0,0,0)
	signal = ut.random_signal(2,10,5)
	p = Gen8(1600, 800, [140,160], (255,255,255), color, signal, 0.01, 15, 34, False, 0.08)
	p.canvas.canvas.show()

#Gen 9
for i in range(1):
	name = "gen9_" + str(i + 1)
	windows = [(160,160,160,50),(120,120,120,50),(90,90,90,50)]
	color = [(60,100,190),(100,70,70)]
	p = Gen9(600, 600, [50,50], (255,255,255), color, 30, windows, 30, False, 5, False)
	p.canvas.canvas.show()

#Gen 10
for i in range(1):
	name = "gen10_" + str(i + 1)
	p = Gen10(500,500,[50,50],(255,255,255),(100,100,100),30,20,5,10)
	p.canvas.canvas.show()

#Gen 13
for i in range(1):
	name = "gen13_" + str(i + 1)
	colors = [(90,90,90,100), (120,120,120,100), (120,60,60,100),(120,90,60,100)]
	p = Gen13(500,500,[100,100],(255,255,255),[6,60],colors,[5,10],0.8,True)
	p.canvas.canvas.show()

#Gen 15
for i in range(1):
	name = "gen15_" + str(i + 1)
	color = (0,0,0)
	p = Gen15(800, 600, (255,255,255), color, 0, [400,300], [200.0,150.0], [1.0, -0.5], 20, True, True, [5,1], 9000, 10)
	p.canvas.canvas.show()

#Gen 16
for i in range(1):
	name = "gen16_" + str(i + 1)
	color = (160,160,160)
	signal = ut.random_signal(0.2,20,3)
	p = Gen16(800, 600, [100,100], (255,255,255), color, [1,1,1], signal, 5, 400, 150)
	p.canvas.canvas.show()

#Gen 17
for i in range(1):
	name = "gen17_" + str(i + 16)
	colors = [(220,30,60),(230,100,100),(120,50,50)]
	p = Gen17(800, 800, [100,100], (255,255,255), colors, 3, 250, 21, 8)
	p.canvas.canvas.show()
