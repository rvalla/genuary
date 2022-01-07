from gen_1 import Gen1
from gen_2 import Gen2
from gen_3 import Gen3
from gen_4 import Gen4
from gen_5 import Gen5
import random as rd

#Gen 1
for i in range(1):
	name = "gen1_" + str(i + 130)
	colors = [(160,160,160),(0,0,0),(50,50,50)]
	p = Gen1(500, 500, [200,400], (255,255,255), colors, [13,0], 1, False)
	p.canvas.canvas.show()

#Gen 2
for i in range(1):
	name = "gen2_" + str(i + 22)
	p = Gen2("assets/input/test.jpg", 50, [100,50], (255,255,255))
	p.canvas.show()

#Gen 3
for i in range(1):
	name = "gen3_" + str(i + 60)
	colors = [(160,160,160),(0,0,0),(50,50,50)]
	t = [0.005,0.03]
	p = Gen3(500, 500, [50,100], (255,255,255), colors, t, 7, 30)
	p.canvas.show()

#Gen 4
for i in range(1):
	name = "gen4_" + str(i + 75)
	colors = [(160,160,160),(0,0,0),(50,50,50)]
	angle_var = [i*3.9,i*-0.3]
	p = Gen4(600,600,[90,60],(255,255,255),colors,0,[300,300],1,8,angle_var,200,False)
	p.canvas.canvas.show()

#Gen 5
for i in range(1):
	name = "gen5_" + str(i + 80)
	colors = [(160,60,160),(0,0,0),(50,160,50)]
	p = Gen5(660, 660, [210,630], (255,255,255), colors, [13,0], 1, False, 500, 3)
	p.canvas.canvas.show()

#Gen 6
for i in range(1):
	name = "gen6_" + str(i + 45)
	color = (100,100,100)
	signal_A = ut.random_signal(3,15,5)
	signal_B = ut.random_signal(-4,15,4)
	p = Gen6(800, 800, [100,100], (0,0,0), color, signal_A, signal_B, 0.01, 120, 10, True, 0.01)
	p.canvas.canvas.show()

#Gen 7
for i in range(1):
	name = "gen7_" + str(i + 26)
	color = (240,0,100)
	p = Gen7(600, 600, [100,100], (255,255,255), color, 10, 5)
	p.canvas.canvas.show()

#Gen 7B
for i in range(1):
	name = "gen7B_" + str(i + 5)
	color = (240,0,100)
	p = Gen7B(600, 600, [100,100], (255,255,255), color, 50, 0)
	p.canvas.canvas.show()

#Gen 8
for i in range(1):
	name = "gen8_" + str(i + 26)
	color = (0,0,0)
	signal = ut.random_signal(2,10,5)
	p = Gen8(1600, 800, [140,160], (255,255,255), color, signal, 0.01, 15, 34, False, 0.08)
	p.canvas.canvas.show()
