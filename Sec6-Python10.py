class Multiplication:
    def __init__(self,a):
        self.firstnumber = int(a)

    def __mul__(self, second_number):
        return self.firstnumber+second_number.firstnumber


mult1 = Multiplication(2)
mult2 = Multiplication(3)

print(mult1*mult2)
