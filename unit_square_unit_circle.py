from random import uniform as rnd
import matplotlib.pyplot as plt

def US_UC(itr):
    # the points generated that land in the unit unit square
    # this is also the total points generated
    unit_square = 0
    # points that land in the unit circle
    unit_circle = 0

    for i in range(itr):
        x = rnd(-1, 1)
        y = rnd(-1, 1)

        circle = x**2 + y**2

        if circle <= 1:
            unit_circle += 1

        unit_square += 1

    return 4*(unit_circle/unit_square)

def vis(itr):
    circle = []
    circley = []
    square = []
    squarey = []
    for i in range(itr):
        x = rnd(-1, 1)
        y = rnd(-1, 1)

        c = x**2 + y**2

        if c <= 1:
            circle.append(x)
            circley.append(y)
        else:
            square.append(x)
            squarey.append(y)
    plt.plot(circle, circley, 'r', square, squarey, 'b')
    plt.show()
