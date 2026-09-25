print('Hello World')
print(67)
print(6.7)
print(True)

print('Hello', 67, 6.7, True)

# this default behaviour is adding a sep = ' ' to the output, if we want to overwrite it, we can just change the sep

# using sep='\n'

print('Hello', 67, 6.7, True, sep="/")

# overriding the default end behaviour
print("Hello", end='-')
print("World")

print(type({1,2,3}))
print(type([1,2,3]))
print(type({'name': "karan"}))

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")


def makeItSpeak(animal):
    animal.speak()

makeItSpeak(Cat())
makeItSpeak(Dog())