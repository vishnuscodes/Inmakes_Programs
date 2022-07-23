class Computer:
    def __init__(self):
        self.Ram = ""
        self.DisplaySize = ""
        self.Processor = ""

    def getspecs(self):
        self.Ram = input("What is the amount of ram? ")
        self.DisplaySize = input("Display size? ")
        self.Processor = input("Processor? ")

    def displayspecs(self):
        print("Ram : " +self.Ram)
        print("Display size : "+self.DisplaySize)
        print("Processor : " +self.Processor)

class Laptop(Computer):
    def __init__(self):
        # super().__init__()
        self.weight = ""

    def getweight(self):
        self.weight = input("What is the weight of the laptop? ")

    def displayweight(self):
        print("Weight : " +self.weight)


class Desktop(Computer):
    def __init__(self):
        super().__init__()
        self.price = ""

    def getprice(self):
        self.price = input("What is the total price of the desktop? ")

    def displayprice(self):
        print("Price : " + self.price)


# computer1 = Computer()
# computer1.getspecs()
# computer1.displayspecs()

laptop1 = Laptop()
laptop1.getspecs()
laptop1.displayspecs()
laptop1.getweight()
laptop1.displayweight()

desktop1 = Desktop()
desktop1.getspecs()
desktop1.displayspecs()
desktop1.getprice()
desktop1.displayprice()