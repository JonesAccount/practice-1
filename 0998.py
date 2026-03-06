numbers = [5, 2, 8, 1, 9, 3, 7]

new = sorted(numbers)

new = (lambda x=new: x[::-1])()
    
print(new)