def is_even(n):
    """
    This function returns a boolean value if 'n' is even, else odd
    input : any valid integer
    output : True/False

    created on 30th Sep 2026
    """
    if(n % 2 == 0):
        return True
    else:
        return False

for i in range(1,11):
    print(i, is_even(i))