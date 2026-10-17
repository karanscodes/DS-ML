# What are functions?
piece of code written to perform specific tasks.

Functions are more practical than theory, so see the programs not the notes. Notes might not have much.

# Error Handling
Basic Error handling in python without Try/Except Method, More in detail later.

```python
def is_even(n):
    """
    Checks whether an integer is even or odd
    Args: 
        n (int): the number to check.

    Returns:
        str: "even" if n is even, "odd" if n is odd,
             "Invalid Input" if n is not an integer.

    created on 30th Sep 2026
    """

    if type(n) == int:
        if(n % 2 == 0):
            return "even"
        else:
            return "odd"
    else:
        return "Invalid Input"
```
## Accessing doc string of a func
To access doc string of a function just do this
```py
# continuing with is.even()
print(is_even.__doc__)
```
# Parameters v/s Arguments
At the time of creation, it's called parameters, when called it's called Arguments
```python

# n below is a parameter to the function
def is_even(n):
    if(n % 2 == 0):
        return "even"
    else:
        return "odd"

# 7 below is an argument to the function
is_even(7)
```

# Types of Arguments
## Default Arguments
This prevents Errors and sets default arguments in our functions as the name suggests
```python
def greet(name='Guest'):
    print(f"Hello {name}")

greet()         # Hello Guest
greet("Karan")  # Hello Karan
```

## Positional Arguments
When we send arguments in python, arguments follow parameters position by Default
```python
def power(a=1, b=1):
    return a**b

print(power(2,3)) 
```
a will be assigned 2, b will be assigned as 3
\
## Keyword Argument
passing arguments with the name of parameter, this could happen if we don't know the postion of the parameters when there are many of them in the function
```python
# continuing with the power() function
power(b=3, a=2)
```

## `*args` and `**kwargs`
**`*args`**
```python
# allows us to pass a variable number of non-keyword arguments to function

def multiply(a,b):
    return a*b

multiply(2,3)
```

Let's say I am making this function for my company and my manager says make this function be able to take any number of arguments

In this case, even I don't know how many arguments will the user input in the function, so this is where args steps in, `*args` allows us to have variable number of parameters/arguments

```python
# when use the '*', python recognises that the number of arguments is variable, and it makes a tuple for it

def multiply(*args):
    product = 1

    for i in args:
        product = product * i
    
    return product
```
args is not a keyword, we can use other names for identifier as well.

---
**`**kwargs`** kw: keyword
- kwargs allows us to pass any number of keyword arguments.
- Keyword arguments mean that they contain a key value pair like a dictionary in python

```python
# just like python converted *args into a tuple, it'll convert **kwargs into a dictionary
def display(**kwargs):

    for (key, value) in kwargs.items():
        print(key, "->", value)

display(india='delhi', srilanka='colombo',nepal='kathmandu',pakistan='islamabad')
```

```
india -> delhi
srilanka -> colombo
nepal -> kathmandu
pakistan -> islamabad
```

Points to remember for `*args` and `**kwargs`
- order of the arguments matter (normal -> *args -> **kwargs)
- The words 'args' and 'kwargs' are just naming convention.

# Function in Memory
How are functions executed in memory?
```python
def is_even(n):
    if(n % 2 == 0):
            return "even"
        else:
            return "odd"
print(is_even(7)) # None
```
function acts like an independent space in memory in a program which in itself has its memory

claude
```
Each function call creates its own stack frame in memory, holding that call's parameters and local variables. The frame is pushed onto the call stack when the function is called and popped when it returns, so its variables disappear.
```

If a function prints something, and we call print for it, it'll get a none value printed as well
```python
def test(n):
    print("true")

print(test(9))
```
```
true
None
```
another one
```python
L = [1,2,3]
print(L.append(4))  # just appends to the list, does not have a return value
print(L)
```
```
None
[1,2,3,4]
```

# Variable Scope
basic global scope vs local scope
```python
def g(y):
    print(x)    
    print(x+1)

x = 5
g(x)
# python will look for x inside the local scope, then enclosing, then global scope

print(x)
# 5 6 5
```
```python
def f(y):
    x = 1   # x is local to f()
    x += 1
    print(x)

x = 5
f(x)
print(x)
# 2 5
```
Important one
```python
def h(y):
    x += 1

x = 5
h(x)
print(x)   
```
This will throw an `UnboundLocalError`, because x is not a local variable, and we cannot change local variables inside the function without getting them locally which by in itself is discouraged.

better explanation: "x is not a local variable" is backwards. Rewrite it as: x += 1 is an assignment, so Python treats x as local to h for the whole function. It then tries to read that local x before it has a value, and raises the error. That's the part you'll want to remember.

to change global variables, we can use global keyword
```python
# This tells python that we are changing global variable x, but this is discouraged.

def h(y):
    global x
    x += 1

x = 5
h(x)
print(x)
```

```python
def f(x):
    x = x + 1
    print('in f(x) : x =', x)
    return x
x = 3
z = f(x)
print('in main scope: z =', z)
print('in main scope: x =', x)
```
```
in f(x) : x = 4
in main scope: z = 4
in main scope: x = 3
```
# Nested Functions
```python
def f():
    def g():
        print('inside function g!')
    g()
    print('inside function f!')

f()
```
you cannot access g() with the main program, we can hide some interesting things inside functions with this.

A tricky question
```python
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(), x is:', x)
    h()
    return x

x = 3
z = g(x)
```
Another tricky example, use this to brush up scope logic!
```python
def g(x):
    def h(x):
        x = x + 1
        print("in h(x), x =", x)
    x = x + 1
    print('in g(x): x=', x)
    h(x)
    return x

x = 3
z = g(x)
print("in main scope, x =", x)
print("in main scope, z =", z)
```

# Functions are 1st class citizens
i.e they support all the operations generally available to other entities

## type and id
```python
def square(n):
    return n**2

type(square)    #function
id(square) #some address
```
function is literally just like any other data type.

## reassign
```python
x = square 
```
now x is a function which acts same as square function

## deleting a Function
```python
del square
```
will it work? yep, can't use `square()` anymore

## storing a function
```python
L = [1,2,3,square]
L[-1](3)    # 9
```
yes this works as well, because function is a first class citizen, which is like any other datatype 

## is function mutable
we can check that with sets, because sets don't allow mutable datatypes to be stored in them
```python
s = {square}
```

the code RAN, which means functions are immutable.

## return a function

```python
def f():
    def x(a,b):
        return a + b
    return x

val = f()(3,4)
print(val)
```
the outer function sent a reference of the inner function as a return value, which we later can invoke and use

## function as an argument

```python
def func_a():
    print("inside function a")

def func_b(z):
    print('inside function b')
    return z()

print(func_b(func_a))
``` 

# Benefits of Functions
- code modularity
- code readability
- code reusability


# Lambda Functions
a lambda function is a small anonymous function

it can take any number of arguments, but can only have one expresion.

```python
# example
lambda a,b : a+b
```

lambda function for a square
```python
# a becomes a function

a = lambda x : x**2
print(a(2))

sum = lambda x,y: x+y
print(sum(3,5))
```

# Lambda v/s Normal function
- no name
- lambda has no return value, it returns a Function
- lambda is written in 1 line
- not reusable

they are with higher order functions

```python
# check if a string has 'a'
check = lambda s : 'a' in s
check('hello') # False

# odd or even
is_even = lambda n : 'even' if n % 2 == 0 else 'odd'
```

# Higher Order functions
a function that returns a function, or takes another function as an input is an higher order function.

```python
def transform(f,L):
    output = []
    for i in L:
        output.append(f(i))
    
    print(output)

L = [1,2,3,4,5]

transform(lambda x:x**2, L)
```

# Map
square the items of a list

```python
print(list(map(lambda x:x**2, [1,2,3,4,5])))
```

odd even 
```python
list(map(lambda n : 'even' if n%2 == 0 else 'odd'), [1,2,3,4,5,6])
```

fetch names
```python
users = [
    {
        'name' : 'karan',
        'age': 21,
        'gender': 'm',
    },
    {
        'name' : 'maansi',
        'age' : 21,
        'gender': 'f'
    },
    {
        'name' : 'keshav',
        'age': 20,
        'gender':'m'
    }
]

list(map(lambda users:users['gender'],users))
```

# Filter
greater than 5
```python
L = [1,2,3,4,5,6,7,8]

print(list(filter(lambda x:x>5, L)))
```

fruits starting with 'a'
```python
fruits = []
print(list(filter(lambda x:x.startswith('a'), fruits)))
```

# Reduce
gotta import functools

```python
import functools

functools.reduce(lambda x,y : x+y, [1,2,3,4,5])

# 15
```

find minimum
```python
import functools

functools.reduce(lambda x, y : x if x < y else y, [1,2,3,4,5,6,7]) # 1
```