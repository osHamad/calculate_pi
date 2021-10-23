def nilakantha(itr):
    pi = 3
    for i in range(1, itr):
        pi -= (-1)**i*4/((i*2)*(i*2+1)*(i*2+2))
    return pi
pi = nilakantha(100000)
print(pi)
