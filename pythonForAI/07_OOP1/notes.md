# OOP

Everything in python is an object.

you don't use procedural applications for real world applications.

OOP is based on the principle of : Generality to Specificity 

The main power of OOP is that OOP gives power to the programmer to make custom data types

- Class
- Object
- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

# Classes and Objects
think of List as a class in python, L is an object based on the List class.

```python
L = [1,2,3]
print(type(L))

L.upper()
```
```
<class 'list'>

AttributionError : 'list' object has no attribute 'upper'
```

think of Class as a Blueprint

Class has two main parts
- Data / Property
- Functions or behaviour

An Object is an instance of the class

Classes are of two types, Built in and User-defined

# Creating an Object
```python
objectname = classname()
```

refer to atm.py

# Methods v/s Functions
Functions inside the class are called Methods
```python
L = [1,2,3]

# this is a function
len(L)

# this is a 'list' method
L.append(4)
```

# Dunder Methods / Magic Methods
Magic (dunder) methods are special methods named with double underscores on both
sides, like `__add__`. Each one is tied to a built-in operation or syntax:
- `__init__` -> object creation
- `__add__` -> `+`
- `__len__` -> `len()`
- `__str__` -> `print()` / `str()`

Python calls them automatically when you use that syntax, so we normally don't call
them directly. By implementing them in our own class, we make its objects behave like
built-in types (e.g. a `Vector` class that supports `v1 + v2`).

Constructor is used to write configuration related code, we connect to internet/server, this code control isn't with the user

## `self` keyword
self is a default parameter in all the methods of the class.

Who can access the methods of a class? it's object ofc, we refer the 'object' inside the class as 'self'

an object and self has the same address, refer to 02_constructor.py

self is an instance of class