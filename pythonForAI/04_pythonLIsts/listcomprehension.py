basket = ['apple', 'guava', 'cherry', 'banana']
my_fruits = ['apple', 'kiwi', 'grapes', 'banana']

new_list = [fruit for fruit in my_fruits if fruit in basket and fruit.startswith('a')]
print(new_list)

L = [[i + j for i in range(1,4)] for j in range(0, 3)]
print(L)

L1 = [1,2,3,4]
L2 = [5,6,7,8]

cart_product = [[f'({i},{j})' for j in L2] for i in L1]
for pair in cart_product:
    print(pair)

cart_product = [f'({i},{j})' for i in L1 for j in L2]
for pair in cart_product:
    print(pair)