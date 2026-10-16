# Theory
types of data used for i/o:
- text : '12345' as a sequence of unicode chars
- binary : 12345 as a sequence of byts of its binary equivalent

Hence there are two types of files we deal with
- Text files : all program files are text files
- Binary Files : images, music, videos, exe Files

How is File I/O is done in most programming languages
- open a File
- read/write data
- close the file

# Basics
```python
f = open('sample.txt', 'r') # read only mode
f = open('sample.txt', 'w') # write mode
f = open('sample.txt', 'a') # append mode

f.close() # make sure to close your files
``` 
if 'sample.txt' doesn't exist, python'll create it

one important thing about 'w' mode
```python
f = open("sample.txt", 'w')     # this overwrites the content of 'sample.txt'

```

using 'with' keyword
- its a good idea to close a file after usage as it will free up the resources
- if we don't close it, garbage collector would eventually do so
- 'with' keyword closes the file as soon as the usage is over