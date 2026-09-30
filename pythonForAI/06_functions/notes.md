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