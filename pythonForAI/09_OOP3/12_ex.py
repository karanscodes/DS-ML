class Parent:
    def __init__(self):
        self._num = 100

    
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var = 200
    
    def show(self):
        print(self._num)
        print(self.var)

c = Child()
c.show()