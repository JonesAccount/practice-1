base = {"name": "Aragorn", "level": 15}
stats = {"hp": 200, "attack": 75, "defense": 50}
meta = {"guild": "Rangers", "level": 20}  # level — дубликат!

characters = {base, stats, **meta}
print(characters)

inventory = ["sword", "shield", "bow", "arrow"]
full_inventory = [i for i in inventory for j in range(3)]
print(); print(full_inventory)