log = (
    "ERROR",
    "Соединение прервано",
    "Повторная попытка не удалась"
)

jog = dict(
        user="Иван",
        ip="192.168.0.1"
        )


def text(title, *log, **jog):
    """
    Вывод на экран произвольных значений
    """
    # Первый блок текста
    print(f"[{title}]\n- " + "\n- ".join(f"{i}" for i in log))
        
    # Второй блок текста
    print("Контекст: " + ", ".join(f"{k}={v}" for k, v in jog.items()))


text(*log, **jog)