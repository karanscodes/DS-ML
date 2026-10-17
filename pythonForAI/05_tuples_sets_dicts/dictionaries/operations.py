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

print('name' in student)

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

print(d.items())
print(d.keys())
print(d.values())

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