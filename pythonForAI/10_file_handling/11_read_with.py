with open('sample05.txt', 'r') as f:
    print(f.read())
    f.seek(0)

    # Buffer will keep count of cursor
    print(f.read(10))
    # next 10
    print(f.read(10))
 
# we can work with huge files with this
big_list = ['hello world\n' for i in range(1000)]

with open('big.txt', 'w') as f:
    f.writelines(big_list)