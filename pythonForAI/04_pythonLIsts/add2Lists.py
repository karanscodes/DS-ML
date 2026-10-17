L = [1,2,3,4,5]

print(L)

L.append([6,7,8])
print(L)

L = [1,2,3,4,5]
L.extend([6,7,8])

print(L)

L.extend("Bhopal")
print(L)

# L.extend(5)
print(L)

print() 
print()

L = [1,3,4,5]
print(L)

# list.insert(whereToInsert, whatToInsert)

L.insert(1, 2)
print(L)

L = [1,2,5,7,0]
print(id(L))

L1 = L.copy()
print(L1)

print(id(L1))