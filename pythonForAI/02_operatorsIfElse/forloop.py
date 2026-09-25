for i in range(0, 10, 2):
    print(i + 1)

for i in range(9, 0, -2):
    print(i)

# for loop can iterate over strings, lists, tuples, sets and dictionaries too
for i in "Bhopal":
    print(i, end=" ")
print()
for i in [1,2,3,4,5]:
    print(i, end=" ")

currPop = 10_000

for i in range(0, 11):
    print(f"Population in {2026 - i}: {int(currPop)}")
    currPop = currPop/1.1
