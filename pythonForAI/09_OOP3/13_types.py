# Types of Inheritance.

# Single
# Multilevel
# Hierarchial
# Multiple
# Hybrid

# Single
class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print("Buying a phone")

class Smartphone(Phone):
    pass

s = Smartphone(80000, 'apple', 10)
s.buy()