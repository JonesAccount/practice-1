def sum(n):
    if n < 10:
        return n
    return n % 10 + sum(n // 10)


print(sum(123))
