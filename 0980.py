def factorial(n):
    if n in (0, 1):
        return n
    else:
        return n * factorial(n - 1)

print(factorial(5))