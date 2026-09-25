One weird thing in python is that

Lists in python can contain any kind of objects

"EVERYTHING IS AN OBJECT IN PYTHON" is something that you'll hear a lot in the future

so for example

```py
L = [1, 2, print, type, input]

print(L)
```
won't throw any error because in python, functions are objects too, so they can be passed just like any other value

# Disadvantages of Python Lists
- slow
- eats up more memory
- risky usage

what is risky usage you might ask? well for beginners, lists are mutable and data can be altered very easily

say 
```py
a = [1,2,3]
b = a

print(a)
print(b)

a.append(4)
print(a)
print(b)
```
this will change both the objects because b just has a reference of a, and it is essentially the same object

to prevent this we use `.copy()` in Lists

```py
a = [1,2,3]
b = a.copy()  # This!!

print(a)
print(b)

a.append(4)
print(a)
print(b)
```

keep in mind that .copy() stores a shallow copy, so nested lists still need to be taken care of with .deepcopy()