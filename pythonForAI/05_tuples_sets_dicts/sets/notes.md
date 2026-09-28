# Introduction
A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed). However, a set is mutable. We can add or remove items from it.

Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

Characterstics:
- unordered
- mutable
- no duplicates
- can't contain mutable data types

## Creating Sets
```py
# empty set
s = set()
```
`s = {}` makes a dictionary in python

```py
# 1D set
s1 = {1,2,3}
print(s1)   # <class 'set'>
```
2D sets aren't possible because we can't have mutable data types inside a set

```py
# heterogeneous set
s = {1, 4.5, True, 'hello'}
```
Here is something  interesting about the set above, 1 and True are considered the same by python, so if we print the set, it'd print
```
{1, 4.5, 'hello'}
```
```py
# using type conversion
s4 = set([1,2,3])
print(s4) # {1,2,3}
```
This is not allowed
```py
s = {1,2,3, [4,5,6]}
print(s)
```
A set cannot have mutable data types, this would give error
```
s = {1,2,2, [1,23,3]}
TypeError: unhashable type: 'list'
```

## Accessing items
since set is unordered, we can't access items via indexing
similarly

## Adding items
add function (for single item)
```py
S = {1,2,3,4}
S.add(5)

print(S) # {1,2,3,4,5}
```
update function (for multiple item)
```py
# make a list of items
S = {1,2,3,4}
S.update([5,6,7])

print(S) # {1,2,3,4,5,6,7}
```

## Deleting items
`del` : keyword, we can literally delete the entire thing

`discard` v/s `remove`
```py
S = {1,2,3,4,5}
S.discard(5)

print(S)
```
discard will discard the mentioned element, if it doesn't find the element, code will not break

but with remove, it has the same functionality as discard, except when the element is not present, in which case, remove throws an error.

`pop` : now this is weird, but .pop() will remove a random element from the set

`clear` : .clear() will empty the set

# Set Operations
- Union(|)
- Intersection(&)
- Difference(-)
- Symmetric Difference(^)
- Membership Test
- iteration

```py
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1 | s2)  # union
print(s1 & s2)  # intersection
print(s1 - s2)  # difference
print(s1 ^ s2)  # symmetric difference (s1 - s2) | (s2 - s1)
```
Symmetric difference is basically s1|s2 - s1&s2 of the sets under operation

*Membership* & *Iteration*
```python
S = {1,2,3,4}

print(8 not in S) # True

for i in S:
    print(i, end=' ') # 1 2 3 4
```

# Set Functions
universal functions : `len` , `sum` , `min` , `max` , `sorted` 

- don't forget that sorted returns a sorted list

`union` function, does the same thing as `|`
```py
S1 = {1,2,3,4}
S2 = {5,6,7,8}

S1.union(S2)

# could also use the .update() function but would change the original set
```
`Intersection` function : does the same thing as `&`
```py
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7,8}

# Same Thing
print(s1 & s2)
print(s1.intersection(s2))

# These might look the same but the first one changes s1, the second one makes a new object altogether
s1.intersection_update(s2)
s1 = s1.intersection(s2)    
```

same with `difference` and `symmetric_difference`
```py
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7,8}

print(s1.difference(s2)) # s1 - s2
print(s1.symmetric_difference(s2)) #{1,2,6,7,8}
s1.symmetric_difference_update(s2)
```
## More Functions

`is_disjoint()` : do they have intersecting elements

`is_subset()`

`is_superset()`

`.copy()`

```py
s1 = {1,2,3,4,5}
s2 = {6,7,8,9}
print(s1.isdisjoint(s2)) # True

s1 = {1,2,3,4,5,6}
s2 = {3,4,5}
print(s2.issubset(s1)) # True
print(s1.issuperset(s2)) # True
```

# Frozen set
is an immutable set in python.

no addition or deletion
```py
# frozenset takes an iterable in its argument
fs1 = frozenset([1,2,3]) # 
```
You can use `frozenset()` when making read only items
2D frozensets are possible
```py
fs = frozenset({1,2,frozenset({3,4})})
```
# Set Comprehension
