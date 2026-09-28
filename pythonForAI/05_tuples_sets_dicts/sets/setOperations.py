s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)

for i in s1:
    print(i, end='')

print(s1.union(s2))
s1.update(s2)
print(s1)

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7,8}
print(s1 & s2)
print(s1.intersection(s2))

s1.intersection_update(s2)
print(s1)

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7,8}

print(s1.symmetric_difference(s2))

print(s1.difference(s2)) # s1 - s2

s1 = {1,2,3,4,5}
s2 = {6,7,8,9}
print(s1.isdisjoint(s2)) # True

s1 = {1,2,3,4,5,6}
s2 = {3,4,5}
print(s2.issubset(s1)) # True
print(s1.issuperset(s2)) # True

