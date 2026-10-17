class Person:

    def __init__(self, name, college):
        self._name = name
        self._college = college

p1 = Person("Karan", "LNCT")
p2 = Person("Adhiraj", "IITKGP")
p3 = Person("Anant", "IIMA")

L = [p1, p2, p3]
print(L)

for i in L:
    print(i._name, 'in', i._college)