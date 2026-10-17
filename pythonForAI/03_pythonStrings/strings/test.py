s = 'hello'
s = "hello"

#multiline strings
s = '''hello'''


# indexing

#positive indexing toh aati h

# negative indexing
s = 'hello world'
print(s[-1], s[-2], s[-3], s[-4])

# slicing
s = 'hello world'
print(s[0:5])
print(s[4:])

# you can even give a third index
print(s[0:7:2])

print(s[6:0:-2])

print(s[::-1])

print(s[-1: -6: -1])

# editing/deleting strings
s = 'hello world'
# del s
print(s)

# Operations on strings

# arithmetic
# '+' does concatenate the strings
# '*' multiplies the strings
print('Bhopal'*3)
print('*'*55)

# relational
print('delhi' == 'bhopal')

# strings are being compared lexicographically
print('delhi' > 'pune')
print('delhi' > 'bhopal')
print('pune' < 'Pune')



#######     WEIRD BEHAVIOUR ALERT ############# 
# if string has chars, then it is True in python, else its false
print('hello' and 'world') # python had to go to the second guy to make sure it's true, therefore world is printed
print('hello' or 'world') # python has to just make sure that the first guy is true, it didn't need to go further hence it printed 'hello'
print('' and 'world')
print('' or 'world')


# loops
for i in 'Bhopal':
    print(i, end='')
print()

for i in 'dehli':
    print('pune')

# membership operators
print('B' in "Bhopal")
print('b' in "Bhopal")