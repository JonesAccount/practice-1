import sys
sys.setrecursionlimit(2222)  # но это не рекомендуется
print(sys.getrecursionlimit())  # 1000


def rec(n=1):
    try:
        n += 1
        print(n)
        rec(n)
    except:
        print("Конец")
    

rec()