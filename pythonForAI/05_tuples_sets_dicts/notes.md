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

print(1 in t1)  # True
```
## iteration
```py
for i in t1:
    print(i,end=' ')    # 1 2 3 4
```

# Tuple Functions
very similar to Lists, in tuples we have

len, sum, min, max, sorted

the first 4 returns an integer, meawhile `sorted(iterable)` always returns a list

```py
t = (1,4,3,2,5)
print(t)

print(len(t))   # 5
print(sum(t))   # 15
print(min(t))   # 1
print(max(t))   # 5

s = sorted(t)
print(s)    # a list

print(tuple(s))
```

`count` & `index` same as in lists 

count returns the count of a member of the tuple

index returns the first occurence, throws an error if DNE


# Difference between Lists and Tuples
- syntax [] vs ()
- mutability
- speed (tuples, which are immutable, generally are faster)
```py
import time
L = list(range(10000000))
T = tuple(range(10000000))

start = time.time()
for i in L:
    i * 5

print("List time:", time.time() - start) 

start = time.time()

for i in T:
    i * 5
print("Tuple time:", time.time() - start)
```
This won't actually work as intended in some cases but the concept is still right, Immutable data types are faster than mutable ones.

- size
```python
L = list(range(1000))
T = tuple(range(1000))

print('List size:', sys.getsizeof(L))
print('Tuple size:', sys.getsizeof(T))
```


- List has more built in functions
- List is more error prone as it's mutable

```py
a = [1,2,3]
b = a

a.append(4)
```
This would change both a and b because they're both pointing to the same object

meanwhile if we use a tuple
```py
a = (1,2,3)
b = a

a = a + (4,)

print(a)    # (1,2,3,4)
print(b)    # (1,2,3)
```

- usability

# Special Syntax (Tuple unpacking)
```py
a,b,c = (1,2,3)
print(a,b,c) # 1 2 3

a,b = (1,2,3)
print(a,b) # Error: too many values to unpack

# there is better method, let's say i only need the first two values
a,b, *others = (1,2,3,4)
print(a, b) # 1 2
print(others)   # This becomes a list [3,4]
```

To swap values, this syntax in python is very common
```py
a = 1
b = 2
a,b = b,a
print(a,b) # 2 1
```

# Zipping Tuples
basically using zip() on tuples
```py
a = (1,2,3,4)
b = (5,6,7,8)

print(tuple(zip(a,b)))
```
