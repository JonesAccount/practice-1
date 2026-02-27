def text(t1, t2, reg=True, trial=1) -> str:
    if trial:
        t1 = t1.strip()
    if reg:
        t1 = t1.capitalize()
    return t1 == t2
    

print(text(t2 = "Python", t1 = " pYtHon    "))