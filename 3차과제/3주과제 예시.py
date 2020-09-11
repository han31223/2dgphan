def ft(a) :
    if a == 1 :
        return 1
    return a * ft(a-1)

print(ft(3))
