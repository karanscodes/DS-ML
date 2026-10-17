# returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in passed iterator is paired together, if the size vary, the shorter one decides the least items of the new iterator

L1 = [1,2,3,4,5,6]
L2 = [-1,-2,-3,-4,-5,-6,-7]

print(list(zip(L1, L2)))

# add two lists of equal size

newList = [i + j for i,j in zip(L1, L2)]
print(newList)