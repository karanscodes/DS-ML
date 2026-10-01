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
    else return "Invalid Input"
```
## Accessing doc string of a func
To access doc string of a function just do this
```py
# continuing with is.even()
print(is.even.__doc__)
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