# 1. Find the length of a string without using the len() function
s = input("Enter the string: ")


length = 0
for i in s:
    length += 1

print(length)

# 2. extract username from an email

email = input("Enter your email: ")

# two methods, one for loop, the other getting the index of '@'
username = ''
for i in email:
    if(i == '@'):
        break
    username += i
print(f'Your Username is {username}')

#method 2
username = ''
i = email.index('@')
print(f'Your Username is {email[:i]}')

# WAP that counts frequency of a character in the string
s = input("Enter the string: ")
c = input("Enter the character who's frequency is to be determined: ")

freq = 0
for i in s:
    if(i == c):
        freq += 1
print(f"The character '{c}' appears {freq} times in the string")

# remove a character from the string
# since python strings are immutable, we must create a new string

string = input("Enter the string: ")
char = input("Enter the character which you want to be removed: ")
result = ''

for i in string: 
    if(i == char):
        continue
    result += i

print(f"Removed character '{char}' from the string : '{string}'\nOutput: '{result}' ")

# Palindrome check
string = input("Enter the string for palindrome check: ")

n = len(string)

for i in range(n//2):
    if(string[i] != string[n - 1 - i]):
        print("Not a Palindrome!")
        break
else:
    print("Palindrome!")

# without split, count the number of words/store them in a list

x = input("Enter a sentence here: ")
tempWord = ''
L = []
for i in x:
    if(i != ' '):
        tempWord += i
    else:
        L.append(tempWord)
        tempWord = ''

if(x[len(x) - 1] == ' '):
    print(L)
else:
    L.append(tempWord)
    print(L)
