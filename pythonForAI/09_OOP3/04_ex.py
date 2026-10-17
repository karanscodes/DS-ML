# When the child has a constructor, Parent's constructor isn't called
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
    
class Smartphone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print("Inside Smartphone Constructor")
    
s = Smartphone("Android", 4)