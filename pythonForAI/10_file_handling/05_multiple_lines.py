L = ['hello', 'how are you?', 'everything alright?', 'you look good', 'have a nice day']

f = open('sample05.txt', 'a')

# writelines take an iterator.
f.writelines(line + "\n" for line in L)
f.close()