class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone!")

class Smartphone(Phone):
    pass

s = Smartphone(50000, "apple", 14)
print(s.price, s.camera, s.brand)
s.buy()