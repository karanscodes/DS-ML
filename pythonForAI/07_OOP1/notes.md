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

# Creating an Object
```python
objectname = classname()
```