import math


def kikuo_takano():
    pi = 4*(12 * math.atan(1 / 49) + 32 * math.atan(1 / 57) - 5 * math.atan(1 / 239) + 12 * math.atan(1 / 110443))
    return pi


t = kikuo_takano()

print(t)