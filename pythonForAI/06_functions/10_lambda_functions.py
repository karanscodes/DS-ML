a = lambda x : x**2
print(a(2))

sum = lambda x,y: x+y
print(sum(3,5))

def transform(f,L):
    output = []
    for i in L:
        output.append(f(i))
    
    print(output)

L = [1,2,3,4,5]

transform(lambda x:x**2, L)


print(list(map(lambda x:x**2, [1,2,3,4,5])))

print(list(map(lambda n : 'even' if n%2 == 0 else 'odd', [1,2,3,4,5,6])))

import functools

print(functools.reduce(lambda x, y : x if x < y else y, [2,3,4,5,6,7])) # 1