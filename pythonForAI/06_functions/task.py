# problem 1
n = int(input("Enter: "))

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
 
# problem 2
n = int(input("Enter: "))

for i in range(1, n + 1):
    for j in