import gen
import random as rd
from gen_util import GenUtil
from PIL import Image as im
import numpy as np
import random as rd
import math

def get_day(day):
  if day == 29:
    print("We are making a Hitomezashi pattern...", end="\n")
    print("Give me a word or a sentence...", end="\n")
    word_a = input()
    print("Give me another word or sentence...", end="\n")
    word_b = input()
    try:
      color = (rd.randint(0,255),rd.randint(0,255),rd.randint(0,255))
      gen.gen_29c((64,64), (100,100), 6, color, (255,255,255), word_a, word_b, str(day))
      print("The pattern was saved!", end="\n")
      gen.gen_29c((64,64), (100,100), 6, color, (255,255,255), word_a + word_a[::-1], word_b + word_b[::-1], str(day) + "s")
      print("I saved a simetric version too!", end="\n")
    except:
      print("I failed! I couldn't creat the patter...", end="\n")
  else:
    print("I am sorry. I don't know what to do with " + str(day) + "...", end="\n")

print("Let's play with Genuary 2025 ideas...", end="\n")
print("You can use the word exit to end this execution...", end="\n")

day = None
d = None

while True:
  print("Tell me which day you are interested in...", end="\n")
  day = input()
  if day == "exit":
    print("Ok, that's all for now...", end="\n")
    break
  else:
    try:
      d = int(day)%31
      print("Ok. Let's work with day " + day + "...", end="\n")
    except:
      print("I think that is not a number...", end="\n")
      continue
    get_day(d)
