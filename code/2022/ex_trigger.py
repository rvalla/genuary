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
