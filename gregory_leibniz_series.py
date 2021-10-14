def leibniz_formula(itr):
    pi = 1
    add = False
    for i in range(3, itr):
        if i%2!=0:
            if add:
                pi+=(1/i)
                add = False
            elif not add:
                pi-=(1/i)
                add = True
    return pi*4

print(leibniz_formula(10000))
