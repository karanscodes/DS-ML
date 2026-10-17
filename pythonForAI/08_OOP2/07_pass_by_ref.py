# Testing more stuff

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
def change_name(person):
    person.name = 'new_name'
    return person
    
guy = Person("Karan", "man")
print(id(guy))

p1 = change_name(guy)
print(id(p1))