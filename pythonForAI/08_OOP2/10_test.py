# The gist is : There is nothing truly private in python.

class Person:
    def __init__(self, name):
        self.__name = name
    
p1 = Person("Karan")
p1.__name = "Twin"

# the thing is, at compile time, variable __name becomes _Person__name

# so _Person__name is storing "Karan", meanwhile
# line 6 creates an entirely new attribute __name and saves it as "Twin", which helps to protect the original data in a way (not really), prevents accidental overwrites by eliminating a clash between names

# but what if we do
p1._Person__name = "Twin"
print(p1.__dict__)  # {'_Person__name': 'Twin', '__name': 'Twin'}