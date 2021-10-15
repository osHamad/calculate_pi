import math

def sin_function(i):
    pi = i*math.sin(math.radians(180/i))
    return pi
pi = sin_function(1000000)
print(pi)
