students = [
    ("Alice", "Math", 85),
    ("Bob", "Math", 78),
    ("Alice", "Physics", 92),
    ("Bob", "Physics", 88),
    ("Charlie", "Math", 90),
    ("Charlie", "Physics", 85)
]

names = {i[0] for i in students}

d = dict(); d = d.fromkeys(names, {})

d = {d[i] = 1 for i in range(len(d))}






print(d)



# {
#     "Alice": {"Math": 85, "Physics": 92},
#     "Bob": {"Math": 78, "Physics": 88},
#     "Charlie": {"Math": 90, "Physics": 85}
# }
