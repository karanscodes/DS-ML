# Arithmetic operators
print(5 + 6)

print(5 - 4)

print(5 * 4)

#always returns float
print(5 / 4)

# integer division
print(5 // 4)

# modulo operation
print(5 % 4)

# exponent
print(5 ** 2)


# Relational Operators
print(4 > 5)
print(3 < 4)
print(3 >= 3)
print(4 <= 4)
print(4 == 4)
print(3 != 4)


#Logical Operators

# AND
print(1 and 0)

# OR
print(1 or 0)

# NOT
print(not 0)


# Bitwise Operators
# they are special operators that operate on binary operators

# bitwise and
print(2 & 3)    # 2

# bitwise or
print(2 | 3)    # 3

# bitwise xor
print(2 ^ 3)    # 1

# bitwise not
print(~60)      # -61, formula is ~x = -(x + 1)

print(4 >> 2) # right shift, shifts all the bits to the right
print(5 << 2) # left shift, shifts all the bits to the left
print(3 <<  2)

# one formula, 
# when shifting right, we can find out the value by dividing by 2**n
# when shifting left, we can find out the value by multiplying by 2**n

## Assignment Operators
a = 2
a += 2

# a++ isn't valid in python


## Membership Operator

# in / not in

print('D' in 'Delhi')

num = 651

sum = 0
sum += num % 10
num //= 10
sum += num % 10
num //= 10
sum += num % 10
print(sum)

# if else in python

# email : karanadityasingh@campusx.com
# pass : 1234

email = input("Enter Your Email: ")
password = int(input("Enter Your Password: "))

if email == "karanadityasingh@campusx.com" and password == 1234:
    print("Welcome User!")
elif email == "karanadityasingh@campusx.com" and password != 1234:
    print("Password Incorrect!")
    password = int(input("Try entering password again: "))
    if(password == 1234):
        print("Welcome User!")
    else: 
        print("Beta tumse na ho payega")
else: 
    print("Invalid Email or Password")

# smallest of three numbers
print("Let's figure out the minimum or 3 numbers")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if(a < b) and (a < c):
    print(a, "is the smallest number!")
elif(b < c):
    print(b, "is the smallest number!")
else:
    print(c, "is the smallest number!")

# making a menu driven program, for example calculator
fnum = int(input("Enter the 1st number: "))
snum = int(input("Enter the second number: "))

op = input("Enter the operation: ")

if op == '+':
    print(f"{fnum} + {snum} = {fnum + snum}")
elif op == '-':
    print(f"{fnum} - {snum} = {fnum - snum}")
elif op == '*':
    print(f"{fnum} * {snum} = {fnum * snum}")
else:
    print(f"{fnum} / {snum} = {fnum / snum}")