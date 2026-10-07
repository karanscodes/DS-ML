# we can add attributes to an object from outside the class as well
class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def greet(self):
        if self.country == 'india':
            print(f"Namaste {self.name}!")
        else:
            print(f"Hello {self.name}!")

p = Person("Karan", "india")

# if we try to access, it'll throw an AttributeError, but if we assign it, it'll become an attribute for that object
p.gender = 'man'
print(p.gender)
print(p)