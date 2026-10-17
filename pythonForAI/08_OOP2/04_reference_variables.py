class Person:
    def __init__(self):
        self.name = "Karan"
        self.gender = "Man"

# will an object be created if I do this
Person()

# The answer is yes, p below stores a reference to the object which is created
p = Person()
q = p
print(id(p), id(q))

print(p.name, q.name)

# since q and p point to the same object, changes from one will have changes in the object they both are pointing to
q.name = "Twin"
print(p.name, q.name)
