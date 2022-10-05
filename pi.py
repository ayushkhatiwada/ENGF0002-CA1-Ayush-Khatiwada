#random.random() generates a number between 0 and 1
#generate (x,y) using random.random()
#check if (x,y) is within the circle by checking if it is within a radius distance (1/2 units) from the centre (1/2, 1/2)
#increas hit by 1 if (x,y) is within circle

import random
from math import sqrt

hits = 0 # amount of points in circle
total = 0 # total points

for i in range(1000000):

    x = random.random()
    y = random.random()

    distance = sqrt( (x - (1/2))**2 + (y - (1/2))**2 )  

    if distance <= (1/2):
        hits += 1

    total += 1

print((hits/total)*4)


