class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print("Buying a phone")

class Smartphone(Phone):
    def buy(self):
        print("Buying a smartphone")
        # we can use parent's methods using 'super'
        super().buy()

s = Smartphone(80000, 'apple', 12)

s.buy()