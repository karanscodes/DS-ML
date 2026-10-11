class Product:
    def review(self):
        print("Product is being reviewed")
    
class Phone(Product):
    def __init__(self, brand, price, camera):
        self.brand = brand
        self.price = price
        self.camera = camera

    def buy(self):
        print("buying a phone")

class Smartphone(Phone):
    pass

s = Smartphone('apple', 100000, 10)
s.buy()
s.review()