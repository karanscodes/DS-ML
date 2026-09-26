# Tuples
A Tuple in python is similar to list. 

The difference being, tuples aren't mutable, Lists are.

**"Tuples are Immutable Lists"**
## Characterstics
- Ordered
- Unchangeable 
- Allows Duplicates

## Creating Tuples
Creating an Empty Tuple is easy.
```py

t1 = ()
print(t1)
print(type(t1)) # <class 'tuple'>
```

Creating a Single Item tuple can cause a minor error

```py
t1 = (1)
print(type(t1)) # <class 'int'>
```

so for single item tuple, use a comma

```py
t1 = (1,)
print(type(t1)) # <class 'tuple'>
```

# Types Of Tuples
## Homogeneous
```py
t1 = (1,2,3,4,5)
```

## Heterogeneous
```py
t1 = (1, 2.5, True, [1,2,3], 3+4j)
```

## 2D Tuple
```py
t5 = (1,2,3, (4,5))
```

## Using Typeconversion
```py
t6 = tuple('hello') # since hello is an iterable, python will separate the characters and create a tuple
print(t6)   # ('h', 'e', 'l', 'l', 'o')
```

# Accessing Items
This is literally same in strings and Lists
## Indexing & Slicing

```py
# indexing
t1 = (1,2,3)
print(t1[0])    # 1
print(t1[-1])   # 3

# slicing
t2 = (1,2,3,4,5)
print(t2[1:4])  # (2,3,4)
print(t2[-3:-1]) # (3,4)
```

# Editing items
if you tried to change an element of the tuple, python would throw an error because tuples are immutable.

# Adding Items
`.append(item)`, `.insert()`, `.extend()` worked in Lists, but not in tuples, because again, tuples are immutable.

# Deleting Items
Deleting the entire tuple works!
```py
t2 = (1,2,3,4,5)
print(t2)

del t2
print(t2)   # t2 not defined
```

but deleting a specific item? not quite something that the tuple would allow
```py
t = (1,2,3,4,67)
del t[-1]   # TypeError: 'tuple' object doesn't support item deletion
```

# Operations on tuples
very similar to lists
## + and *
```py
t1 = (1,2,3,4)
t2 = (5,6,7,8)
print(t1 + t2)  # (1, 2, 3, 4, 5, 6, 7, 8)
print(t1 * 3)   # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
```
## membership
```py
t1 = (1,2,3,4)
t2 = (5,6,7,8)
print(t1 + t2)  # (1, 2, 3, 4, 5, 6, 7, 8)
print(t1 * 3)   # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

print(1 in t1)  # True
```
## iteration
```py
for i in t1:
    print(i,end=' ')    # 1 2 3 4
```

# Tuple Functions
