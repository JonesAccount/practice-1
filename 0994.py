from random import randint as r

nums = [r(1, 20) for i in range(20)]
target = r(5, 10)
result = []

for i in nums:
    for j in nums:
        if i + j == target:
            if (i, j) not in result and (j, i) not in result:
                result.append((i, j))
print(f"Target: {target}")
print(result)