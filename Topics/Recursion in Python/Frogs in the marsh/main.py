def number_of_frogs(year):
    if year == 1:
        return 120         
    return (number_of_frogs(year - 1) - 50) * 2
