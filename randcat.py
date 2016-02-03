import random

random.seed()

while True:
    print(chr(random.getrandbits(8)), end='')
