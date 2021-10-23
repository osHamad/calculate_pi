import math

def stormer():
    pi = 4 * (44 * math.atan(1 / 57) + 7 * math.atan(1 / 239) - 12 * math.atan(1 / 682) + 24 * math.atan(1 / 12943))
    return pi

print(stormer())