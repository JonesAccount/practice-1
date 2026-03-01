def func(n, *args, **kwargs) -> str:
    print(n, args, kwargs)
    
func(1, 2, 55, name = "Alice", true = True)