a, b = 34, 48


def evclid(x, y):
    if x > y:
        d = x
        c = x / y
    else:
        d = y
        c = y / x
        
    while True:
        c = d / c
        
        if c == 0:
            print(y)
            break
        else:
            d /= c
        

evclid(a, b)