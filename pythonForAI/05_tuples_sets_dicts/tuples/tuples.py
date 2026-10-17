# Empty Tuple
t1 = ()
print(type(t1)) 

# Single Item Tuple
t1 = (1)
print(type(t1))

t1 = (1,)
print(type(t1))

t4 = (1, 2.5, True, [1,2,3], 3+4j)
print(type(t4))
 
t6 = tuple('hello') # since hello is an iterable, python will separate the characters and create a tuple
print(t6)

# Accessing Items
# indexing
t1 = (1,2,3)
print(t1[0])    # 1
print(t1[-1])   # 3

# slicing
t2 = (1,2,3,4,5)
print(t2[1:4])  # (2,3,4)
print(t2[-3:-1]) # (3,4)

print(t2)

del t2
# print(t2)   # t2 not defined
t2 = (1,2,3)
# del t2[-1]  # TypeError: 'tuple' object doesn't support item deletion
print(t2)
