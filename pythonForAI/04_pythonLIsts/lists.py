# WHAT ARE LISTS
# They are data types that can store multiple items under 1 name

L = [1,2,3]

print(id(L))

for i in L:
    print(id(i), end=' ')

print()

print(id(1))
print(id(2))
print(id(3))


# very interesting program
import sys
L = []
for i in range(10):
    L.append(i)
    print(len(L), sys.getsizeof(L))

L = [1000, 1000]
for i in L:
    print(id(i), end= " ")

print()

x = [1,2]
L = []
L.append(x)
L.append(x)
for i in L:
    print(id(i), end=" ")

