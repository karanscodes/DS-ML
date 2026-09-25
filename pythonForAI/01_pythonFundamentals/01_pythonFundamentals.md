# Why Python?

1) python design philosophy is unique
- easy syntax
- readable code

2) python comes with batteries included i.e. 
- we can do a lot of stuff which is included in python, in other languages we might have to write extra code

3) Python is a general purpose programming language, we can make ANY type of software with it.

4) Libraries/Community : we don't need to code from scratch

## Why Python for Data Science?
- easy to learn
- proximity with maths
- libraries/Communities


python is case sensitive

# Basic Code
refer the .py file


`print` function
```py
print('Hello', 67, 6.7, True)
```
`sep` keyword

`end` keyword

# Data Types
- Integers `int` : python can handle large integers, python can handle integers upto 1e308], but it depends on the machine would be better description

- Decimals `float` : python can handle decimal upto .1e308

- Strings `str` : python doesn't have a char datatype

- Boolean `bool` : True and False

- Complex Number : example 5+3j

Advanced
- List : equivalent to array
, example : [1,2,3,4,5]

- Tuple : similar to list but immutable, example : (1,2,3,4,5)

- Sets : example : {1,2,3,4,5}

- Dictionary : key-value pair, example : {'name' : 'Karan', 'age' : 21, 'city' : 'Bhopal'}

`type` function

# Variables
## Static Vs Dynamic Typing

- **Static typing** (C, Java): variable's type is fixed at compile time and declared explicitly. Can't change type later.
- **Dynamic typing** (Python): type is tied to the *value*, not the variable, and is checked at runtime. Same variable can hold different types over its lifetime.

```python
x = 5        # int
x = "hello"  # str — no error, allowed in Python
```

## Static Vs Dynamic Binding

- **Static binding**: which function/method gets called is decided at compile time (based on declared type).
- **Dynamic binding**: which method gets called is decided at **runtime**, based on the actual object — not the variable's declared type. This is what makes polymorphism work.

```python
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

animal = Cat()
animal.speak()   # Meow

animal = Dog()
animal.speak()   # Woof
```

Same line `animal.speak()` — but which `speak()` runs is resolved at runtime by checking what `animal` actually is.

> Note: dynamic typing = variable holding different *values/types*.
> Dynamic binding = which *method* runs, resolved at runtime.
> Easy to conflate the two since both are runtime-resolved, but they're different concepts.

## Stylish Declaration Techniques

```py
a,b,c = 1,2,3

a = b = c = 0

```

## Comments
do NOT forget to add comments while writing your code

# Keywords & Identifiers
basically keywords are reserved words that help the interpreter to understand and use to convert code to machine code

never use these words in variables

identifiers cannot be keywords

you cannot start a variable name with a digit

you can use special characters like _

# User Input
WAP to add 2 numbers by taking input

be careful, `input` by default makes the input into a string, so if we want to store an integer, use type conversion

# Type Conversion
## Implicit TC
example

```py
print(5 + 6.7)
```

even though they have different data types, python 'implicitly' converted the value to give accurate answer

## Explicit TC
```py
# example str -> int
a = 5
print(type(a))
b = int(a)
print(type(b))
```

# Literals
Any raw value typed into the code is a literal

## Typical Literals
| Literal Type | Example | Description |
|---|---|---|
| int | `5` | int literal |
| float | `6.7` | float literal |
| string | `"hello"` | string literal |
| bool | `True` | bool literal |
| None | `None` | None literal |
| complex | `3+4j` | complex literal |

## Collection Literals
| Literal Type | Example | Description|
| --- | --- | --- |
| list | `[1, 2, 3]` | list literal |
| tuple | `(1, 2, 3)` | tuple literal |
| set | `{1, 2, 3}` | set literal |
| dict | `{"a": 1, "b": 2}` | dict literal |

## Special Numeric literals
| Literal Type | Example | Description |
|---|---|---|
| binary | 0b1010 | binary literal
| octal | 0o12 | octal literal |
| hexadecimal | 0x1A | hexadecimal literal |
| | 1_000_000 | underscore for readaability (=1000000)|

## Scientific Notation
| Example | Denotes |
|---|---|
| 1.5e2 | 1.5 * 10^2 |
| 1.6e-3 | 1.6 * 10^-3 |

## String Literals
```py
string = 'This is python'
strings = "This is Python"
char = "C"
multilineString = """this is multiline 
string """
rawStr = r"raw \n string"
```

## Boolean Literal
```py
a = True + 4
b = False + 10

print("a:", a)
print("b:", b)
```
## None Literal
since there is no way to declare variables without assigning a value, we can use `None` without getting an error
```py
a = None
print(a)
```