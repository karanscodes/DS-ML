def func_a():
    print("inside function a")

def func_b(z):
    print('inside function b')
    return z()

print(func_b(func_a))