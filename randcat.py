#! /usr/bin/python3
import random

random.seed() # this initializes with the Date, which I think is a novel enough seed

while True: # if we're going with a mimicing of cat /dev/random, it'll pretty much just go until it's killed
    print(chr(random.getrandbits(8)), end='') 
