class Person:

    def __init__(self, name, country):
        self.name = name
        self.country = country
    
p1 = Person("Karan", "India")
p2 = Person("Maansi", "Japan")

# instance variable "name", has different 'names' depending upon the object.
print(p1.name, p2.name)