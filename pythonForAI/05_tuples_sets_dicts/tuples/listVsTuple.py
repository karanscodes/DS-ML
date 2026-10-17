import time
import sys

# time comparison
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


# size comparison
L = list(range(1000))
T = tuple(range(1000))

print('List size:', sys.getsizeof(L))
print('Tuple size:', sys.getsizeof(T))

# A simple doubt regarding 'a'
a = (1,2,3)
b = a

print(id(a))

a = a + (4,)    # this a is completely different than the previous one, concatenation creates a new object and it is assigned to a variable 'a'
print(id(a))
print(id(b))

a,b, *others = (1,2,3,4)
print(a, b)
print(others)


a = (1,2,3,4)
b = (5,6,7,8)

print(zip(a,b))

print(tuple(zip(a,b)))