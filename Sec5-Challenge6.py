def StudentDisount(price):
    return (price - ((10*price)/100))


def RegularDiscount(price):
    return ((price - ((5*price)/100)))



print(RegularDiscount(StudentDisount(20)))