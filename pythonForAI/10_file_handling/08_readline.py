f = open('sample.txt', 'r')

# reading two lines
print(f.readline(), end='')
print(f.readline(), end='')

f.close()
# readline() tab use karte h when we have too much content, meanwhile, we can use read() for smaller programs.