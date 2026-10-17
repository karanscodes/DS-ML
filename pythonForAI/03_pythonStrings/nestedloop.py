n = int(input("Enter n: "))

for i in range(0, n ):
    for j in range(0, i + 1):
        print("*", end="")
    print()

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()