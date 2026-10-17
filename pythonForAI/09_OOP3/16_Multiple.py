class A:
    def __init__(self, price, brand, cam):
        print("Inside A")
        self.price = price
        self.brand = brand
        self.cam  = cam
        
    def buy(self):
        print("A, buying a phone")
    
class B:
    def review(self):
        print("B, Under Review")

class C(A, B):
    pass

c = C(1000, 'apple', 10)
c.buy()
c.review()