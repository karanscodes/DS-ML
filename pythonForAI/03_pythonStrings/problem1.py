n = int(input("Enter n: "))

fact = 1
result = 1
resultStr = "1/1!"
for i in range(2, n + 1):
    fact *= i
    result += i/fact
    resultStr += f" + {i}/{fact}"

print(resultStr)
print(round(result, 2))

