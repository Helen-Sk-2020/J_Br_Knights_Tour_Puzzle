def func(x, y):
    # base case
    if x < y:
        return x
    
    else:
        return func(x - y, y)


print(func(20, 5))  # 0