# guessing game will have a random number, setting the bounds between 1 and 100
import random
jackpot = random.randint(1,100)

# attempt tracker
numOfAttempts = 1

# welcome the user
print('Guess the lucky number!')

guess = int(input("Your Guess Here: "))
while(guess != jackpot):
    numOfAttempts += 1
    if(guess < jackpot):
        print(f"'{guess}' is lower, Guess Higher again!")
    else:
        print(f"'{guess}' is higher, Guess Lower again!")
    guess = int(input("Your Guess Here: "))
else:
    print(f"You did it!\nNumber of attempts : {numOfAttempts}")