t = (1,4,3,2,5)
print(t)

print(len(t))
print(sum(t))
print(min(t))
print(max(t))

s = sorted(t)
print(s)    # a list

print(tuple(s))


t = (1,2,3,4,4,5,6,5,6,5)
print(t.count(10))
print(t.index(10))  # will throw an error 