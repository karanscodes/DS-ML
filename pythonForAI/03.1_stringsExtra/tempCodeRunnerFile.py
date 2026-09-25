s = input("Enter the string: ")
c = input("Enter the character who's frequency is to be determined: ")

freq = 0
for i in s:
    if(i == c):
        freq += 1
print(f"The character '{c}' appears {freq} times in the string")