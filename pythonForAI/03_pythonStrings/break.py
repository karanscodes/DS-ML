#for else loop
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

for i in range(lower, upper + 1):
    for j in range(2, i):
        if(i % j == 0):
            break
    else:
        print(i)

# continue statement
for i in range(1, 10):
    if(i == 5):
        continue
    print(i)

# pass, in cases when you aren't coding up the logic inside the loop, you could just use 'pass' to prevent code from breaking and throwing errors
for i in range(1,10):
    pass