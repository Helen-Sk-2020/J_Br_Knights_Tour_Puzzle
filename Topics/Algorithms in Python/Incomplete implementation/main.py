def startswith_capital_counter(names):
    # number of names
    n = 0
    # s = ""
    # s[0].isupper()

    for name in names:
        if name[0].isupper():
            n += 1
    
    return n
    