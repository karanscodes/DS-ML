# understanding self
class Temp:
    def __init__(self):
        print("id:",id(self))

obj = Temp()
print(id(obj))

obj2 = Temp()
print(id(obj2))