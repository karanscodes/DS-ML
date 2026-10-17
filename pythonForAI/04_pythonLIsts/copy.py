a = [1,2,3]

b = a

print(a)
print(b)

b.append(4)

print(a)
print(b)

a = [1,2,3]
b = a.copy()

b.append(4)

print(a)
print(b)
