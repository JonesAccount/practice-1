value = 1
counter = 1
def factorial(n) -> int:
    global value, counter
    if n in (0, 1):
        return n
    else:
        if counter != n:
            counter += 1
            value *= n + 1
            factorial(n - 1)

res = factorial(int(input("Число: ")))
print(value)