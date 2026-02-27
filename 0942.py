import os

keys = [i for i in range(1, 10)]
game = {}; game = game.fromkeys(keys, "::")

counter = 0
print("Крестики-нолики\n")
for i in range(1, len(keys) + 1):
    print(f"{game[i]} | ", end="")
    counter += 1
    if counter == 3:
        print(); counter = 0
print("\n")
    
def play():
    pass

#os.system("cls" if os.name == "nt" else "clear")