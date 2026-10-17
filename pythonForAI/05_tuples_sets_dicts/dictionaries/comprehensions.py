d = { i : i**2 for i in range(1,11)}
for key in d:
    print(key,":",d[key])

distances = {
    'delhi': 1000,
    'mumbai': 2000,
    'bangalore': 3000,
    }

distancesInMiles = {key:value*0.62 for (key, value) in distances.items()}
print(distancesInMiles)

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

temp_C = [30.5, 32.6, 33.0, 29.8, 28.9, 31.2, 30.9]

d = dict(zip(days, temp_C))
print(d)

# also
test = {i:j for (i,j) in zip(days,temp_C)}
print(test)

products = {
    'phone': 10,
    'laptop': 0,
    'charger': 32,
    'tablet': 0,
}

print({key: val for (key,val) in products.items() if val > 0})


print({i:{j : i*j for j in range(1,11)} for i in range(2,5)},end=" ")