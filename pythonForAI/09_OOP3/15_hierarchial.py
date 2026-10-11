class Phone:
    def __init__(self, brand, price, camera):
        self.brand = brand
        self.price = price
        self.camera = camera

    def buy(self): 
        print("Buying a phone")

class Smartphone(Phone):
    pass

class FeaturePhone(Phone):
    pass

Smartphone('apple', 100000, '10px').buy()
FeaturePhone('lava', 10000, '4px').buy( )