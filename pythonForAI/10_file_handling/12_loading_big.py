with open('big.txt', 'r') as f:
    chunk_size = 10
    chunk = f.read(chunk_size)

    while len(chunk) > 0:
        print(chunk, "***")
        chunk = f.read(chunk_size)