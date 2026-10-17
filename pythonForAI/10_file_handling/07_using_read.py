f = open('sample05.txt', 'r')
s = f.read()
print(s)
print(type(s))

# if i want to read only the first ten characters
f.seek(0)   # seek is used because f.read() read the entire file and the curson is at the end
t = f.read(10)
print(t)
f.close()

