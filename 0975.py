from time import sleep

def f3():
    sleep(2)
    
def f2():
    sleep(2)
    
def f1():
    print("Первая функция")
    f2()
    print("Вторая функция")
    f3()
    print("Третья функция")
    

f1()