class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    
class Smartphone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside Smartphone Constructor")

s = Smartphone(20000, 'samsung', 20, 'android', 8)

print(s.os)
print(s.brand)

# super cannot be used outside class
# super cannot access parent's instance variables
# super is used inside the child class