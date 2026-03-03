def f4(x):
    print(f"{x}. Вперед")
    print(f"{x - 1}. Назад")
    

def f3(x):
    print(f"{x}. Вперед")
    f4(x + 1)
    print(f"{x - 1}. Назад")
    
    
def f2(x):
    print(f"{x}. Вперед")
    f3(x + 1)
    print(f"{x - 1}. Назад")
    
    

def f1(x):
    print(f"{x}. Вперед")
    f2(x + 1)
    print(f"{x - 1}. Назад")
    

f1(1)