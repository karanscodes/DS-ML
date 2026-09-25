def checkPrime(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

for i in range(lower, upper + 1):
    if(checkPrime(i)):
        print(i)
# This could also be written with break statement