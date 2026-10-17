# child object cannot access private data of parent

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside the 'Phone' constructor!")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def show(self):
        print(self.__price)

class Smartphone(Phone):
    def check(self):
        print(self.__price)

s = Smartphone(200000, "apple", 11)
# s.check()
print(s.brand)
s.show()