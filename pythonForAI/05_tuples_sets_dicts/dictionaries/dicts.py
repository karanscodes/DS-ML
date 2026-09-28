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

print(student)

d = dict([('name','karan'), ('age',21), ('college','LNCT')])
print(d)

# could use with 
l1 = ['name', 'age', 'college']
l2 = ['karan', 21, 'LNCT']

d = dict(zip(l1,l2))
print(d)

d = {
    'name': 'Karan',
    'name': 'chor',
}
print(d) # {'name': 'chor'}

my_dict = {
    'name' : 'Karan',
    'age': 21, 
    'college': 'LNCT',
}

print(my_dict['name'])
print(my_dict.get('name'))

print(my_dict['age'])
print(my_dict.get('age'))

d = {
    'name' : 'Karan',
    'age': 21, 
    'college': 'LNCT',
}

print(d)

d['gender'] = 'man'

print(d)

d = {
    'name' : 'Karan',
    'age': 21, 
    'college': 'LNCT',
}
d.pop('college')
print(d)

d = {
    'name' : 'Karan',
    'age': 21, 
    'college': 'LNCT',
}
d.pop('college')
print(d)

d = {
    'name' : 'karan',
}

d.clear()
print(d) # {}