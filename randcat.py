#! /usr/bin/python3
import calendar
import time

seed = calendar.timegm(time.gmtime()) # We'll use the epoch time as a seed.

def random (seed):
    seed2 =  (seed*297642 + 83782)/70000
    return int(seed2) % 70000;
    
    
p = seed
while True: # if we're going with a mimicing of cat /dev/random, it'll pretty much just go until it's killed
    p = random(p)
    print(chr(p % 256), end="")
    p = p % 4000
