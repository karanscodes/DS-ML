# Method Overriding
class Phone:
    def __init__(self, price, brand, camera):
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class Smartphone(Phone):
    def buy(self):
        print("Buying a Smartphone")

s = Smartphone(80000, 'apple', 12)
s.buy()