from random import randint as r

a, b = r(20, 80), r(20, 80)

def evclid(x: int, y: int):
    """
    Описание:
    Вычисляет наибольший общий делитель (НОД) двух чисел методом вычитания.
    Параметры:
    x (int): первое натуральное число
    y (int): второе натуральное число
    Возвращает:
    int: наибольший общий делитель чисел x и y
    """
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x

print(f"НОД {a} и {b} равен {evclid(a, b)}")

helping = input()
if helpib == "1":
    print(help(evclid))