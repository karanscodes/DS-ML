# giving object as an input to a function
class Person:
    def __init__(self, name, role, company):
        self.name = name
        self.role = role
        self.company = company
    
def greet(person):
    print(f"Hi, My name is {person.name}, I am an {person.role} at {person.company}")
    # Extra
    p1 = Person("Kartik", "SDE", "Microsoft")
    return p1

guy = Person("Karan", "SDE", "Amazon")
guy2 = Person("Twin", "SDE", "Google")

greet(guy2)

x = greet(guy)
print(x.name, x.company, x.role)