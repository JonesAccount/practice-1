math = {"Аня", "Борис", "Вика", "Глеб", "Даша"}
physics = {"Вика", "Глеб", "Егор", "Женя"}

print(f"Ходят на математику: {math.difference(physics)}")
print(f"Ходят на физику: {physics - math}")
print(f"Ходят на обе: {math & physics}")