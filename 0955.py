from time import time, sleep
import os


def factorial(number) -> float:
    """
    Пусто
    """
    start_timer = time()
    
    result = 1
    for n in range(1, number + 1):
        result *= n
        print(".")
        os.system('cls' if os.name == 'nt' else 'clear')
        sleep(0.1)
        
    end_timer = time()
    
    return start_timer, end_timer
    

def factorial_test(func) -> str:
    """
    Пусто
    """
    start, end = func(100000)
    
    print(f"Начало: {start}\nКонец: {end}")
        
    if (round(end - start)) < 5:
        print("Результат: радует :)")
    else:
        print("Результат: не радует :(")
        
    
factorial_test(factorial)