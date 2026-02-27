def text(t1, reg=True, trial=1) -> str:
    if trial:
        text = t1.strip()
    if reg:
        text = text.capitalize()
    return text
    

print(text(" pYtHon    "))