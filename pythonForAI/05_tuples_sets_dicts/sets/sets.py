# Creating Set

# Empty set
s = {}
print(s)
print(type(s)) # is a dictionary

s = {1, 4.5, True, 'hello', (1,2,3)}
print(s)

s = {1,2,3,4,1,2,3}
print(s)

# s = {1,2,2, [1,23,3]}

s1 = {1,2,3}
s2 = {3,2,1}
print(s1 == s2)


S = {1,2,3,4}
S.add(5)
print(S)

S.update([6,7,8])
print(S) 
