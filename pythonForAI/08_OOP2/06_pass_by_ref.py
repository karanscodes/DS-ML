# giving object as an input to a function
class Person:
    def __init__(self, name, role, company):
        self.name = name
        self.role = role
        self.company = company
    
def greet(person):
    print(id(person))
    print(f"Hi, My name is {person.name}, I am an {person.role} at {person.company}")

guy = Person("Karan", "SDE", "Amazon")
print(id(guy))
greet(guy)