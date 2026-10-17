class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num
    
class Child(Parent):

    def show(self):
        print("This is in Child Class")

c = Child(100)
print(c.get_num())
c.show()