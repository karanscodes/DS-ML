# seek and tell function

# 'tell' tells where the cursor is
# 'seek' changes the cursor position

with open('sample05.txt', 'r') as f:
    print(f.read(10))
    print(f.tell())
    f.seek(0)
    print(f.read(10))
    print(f.tell())