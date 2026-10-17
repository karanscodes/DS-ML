# Introduction
Dictionary in python is a collection key-value pairs. <br>
Used to store data values like a map <br>
In some languages it is known as map or associative arrays.

```python
d = {
    'name': 'Karan',
    'age': 21,
    'gender': 'man',
}
```

## Characteristics
- mutable
- Indexing has no meaning
- Keys can't be duplicate
- Keys can't be mutable items

# Creating Dictionary
```python
# Empty Dictionary
d = {}

# 1D Homo Dictionary
d1 = {
    'name' : 'karan',
    'gender' : 'male',
}

# Mixed Dictionary
d = {
    'name' : 'karan',
    'age' : 21,
    'gender' : 'male',
}

# 2D dictionary -> JSON
student = {
    'name' : 'Karan',
    'college' : 'LNCT',
    'sem' : 4,
    'subjects' : {
        'dsa' : 100,
        'math' : 67,
        'english' : 80,
    }
}
```

Using Sequence and dict function
```python
d = dict([('name','karan'), ('age',21), ('college','LNCT')])
print(d)

# could use with 
l1 = ['name', 'age', 'college']
l2 = ['karan', 21, 'LNCT']

d = dict(zip(l1,l2))
print(d)
```

in case of Duplicates
```python
d = {
    'name': 'Karan',
    'name': 'chor',
}
print(d) # {'name': 'chor'}
```

# Accessing Items
## 1D Keys
square bracket notation `dict[key]` vs `dict.get(key)`, if the key DNE, the first throws KeyError, and latter doesn't.
```python
my_dict = {
    'name' : 'Karan',
    'age': 21, 
    'college': 'LNCT',
}

print(my_dict['name'])
print(my_dict.get('name'))

print(my_dict['age'])
print(my_dict.get('age'))
```
## Nested keys
```python
student = {
    'name' : 'Karan',
    'college' : 'LNCT',
    'sem' : 4,
    'subjects' : {
        'dsa' : 100,
        'math' : 67,
        'english' : 80,
    }
}

# For accessing the marks of 'math'
student['subjects']['math']

# similarly if you want to add / modify a subject
student['subjects']['data_science'] = 75
```

# Adding key-value pairs
```python
d = {
    'name' : 'Karan',
    'age': 21, 
    'college': 'LNCT',
}

print(d)

# This add a new key / modifies an older one
d['gender'] = 'man'

print(d)
```
# Removing key-value pairs
`.pop(key)` and `.popitem()` returns the key, and (key,val) tuple respectively.

`.pop(key)` 
```python
d = {
    'name' : 'Karan',
    'age': 21, 
    'college': 'LNCT',
}

d.pop('college')
print(d)
```
`d.popitem()` deletes last key-val pair
```py
d = {
    'name' : 'Karan',
    'age': 21, 
    'college': 'LNCT',
}

d.popitem()
print(d)
```
`del` : delete individuals keys!
```python
d = {
    'name' : 'Karan',
    'age': 21, 
    'college': 'LNCT',
}

del d['name']
```
`.clear()` empties the Dictionary
```python
d = {
    'name' : 'karan',
}

d.clear()
print(d) # {}
```
# Editing key-value pairs
I have already gone through this above, go through it in Nested Keys

# Dictionary Operations
everything is about 'keys', values aren't that important.
## Membership 
```python
student = {
    'name' : 'Karan',
    'college' : 'LNCT',
    'sem' : 4,
    'subjects' : {
        'dsa' : 100,
        'math' : 67,
        'english' : 80,
    }
}

print('name' in student)    # True
```
## Iteration
```python
d = {
    'name': 'Karan',
    'age' : 21,
    'gender' : 'man',
    'college' : 'LNCT',
}

# This would print all the keys
for i in d:
    print(i)

# wants key-val pairs?
for key in d:
    print(key, d[key])
```

# Dictionary Functions
`len` : tells the number of keys <br>
`sorted` : sorts all the keys and return a sorted list of keys <br>

Important Functions: `items`, `keys`,  `values`

`.items()` returns a live 'view object' of the dict's (key, value) tuple pairs. Sort of reverse of `dict([pairs])`
```python
d = {
    'name': 'Karan',
    'age' : 21,
    'gender' : 'man',
    'college' : 'LNCT',
}

print(d.items())

print(d.keys())
print(d.values())
```
`update` : if you want to update a dictionary with key value pairs of other
```python
d1 = {
    1:2,
    2:3,
    3:4,
    4:5,
}
d2 = {
    3:67,
    4:69,
}
d1.update(d2) # d1 ko update karo d2 ki values se
print(d1)
```
```
# {1: 2, 2: 3, 3: 67, 4: 69}
```

# Dictionary Comprehension
Nothing new, just the syntax differs a little.
```
{ key : val for vars in iterable}
```

```python
# print 1st 10 numbers and their squares
d = { i : i**2 for i in range(1,11)}
print(d)
```

Making dict using existing dictionaries
```python
distances = {
    'delhi': 1000,
    'mumbai': 2000,
    'bangalore': 3000,
    }

distancesInMiles = {key:value*0.62 for (key, value) in distances.items()}
print(distancesInMiles)
```

using .zip()
```python
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

temp_C = [30.5, 32.6, 33.0, 29.8, 28.9, 31.2, 30.9]

d = dict(zip(days, temp_C))
print(d)

test = {i:j for (i,j) in zip(days,temp_C)}
print(test)
```

Using if condition
```python
products = {
    'phone': 10,
    'laptop': 0,
    'charger': 32,
    'tablet': 0,
}

print({key: val for (key,val) in products.items() if val > 0})
```

## Nested Comprehension
print tables of number from 2 to 4
```python
print({i:{j : i*j for j in range(1,11)} for i in range(2,5)},end=" ")
```

# THE END