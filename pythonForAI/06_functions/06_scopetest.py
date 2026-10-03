def f(x):
    x = x + 1
    print('in f(x) : x =', x)
    return x

x = 3
z = f(x)
print('in main scope: z =', z)
print('in main scope: x =', x)