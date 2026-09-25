# common functions (to strings, sets, dicts, lists)

# len
print(len('hello world'))

# max : will get the max value on the basis of ASCII
# min : will get the min value on the basis of ASCII

print(max('hello world'))
print(min('hello world'))

# sorted : returns a sorted list
sortedList = sorted('hello world')
for i in sortedList: 
    print(i,end=",")

# sort in decreasing order
sortedInReverse = sorted('hello, world', reverse=True)
for i in sortedInReverse:
    print(i, end=",")

print()

# Functions relevant to strings
s = 'hello world'

print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())

print("KaRaNAdiTyaSiNgh".swapcase())

# count, find, index
print('my name is karan'.count('a'))
print('my nane is karan'.find('karan'))
print('name is karan'.find('sanity')) # will give -1
print('my name is karan'.index('is'))

# if you try access something that doesn't exist with index, it'll throw an error
# print('name'.index('karan')) // substring not found

s = 'my name is karan'
print(s.startswith('my'))
print(s.endswith('an'))


# format function/ f string
name = "karan"
age = 21
print(f"hi! my name is {name} and my age is {age}")

# isalnum : isalphanumeric
s = 'karan123'
print(s.isalnum())

s = 'karan1234%$'
print(s.isalnum())

s = '123'
print(s.isdigit())

s = 'karan'
print(s.isalpha())

# check variable names
print('1name'.isidentifier())


#split, join VERY IMP
words = 'hello my name is karan'.split(' ')
for word in words:
    print(word,end=',')
print()
print()


moreWords = 'hello my name is karan'.split('name')
for word in moreWords:
    print(word,end=' ')
print()
print()


# join is reverse of split
print("-".join(words),end=",")
print("$$")

# replace, would replace a substring

s = 'hi my name is karan'
print(s.replace("karan", "nitish"))

# strip VERY USEFUL
s = '         karan         '
print("-",end='')
print(s.strip(), end='')
print("-",end='')