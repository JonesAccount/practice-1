def func(arg1, *args, **kwargs):
    print(f"arg1: {arg1}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

n = False
n1 = not False
tup = (4, 5, 6, 7, n, n1)
print(tup)
func(i for i in tup)