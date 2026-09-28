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

## Characterstics
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
    age : 21,
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

`.items()` breaks key-val pairs into tuple pairs and returns a 'view object' of all the tuple pairs
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