import random
n = random.randint(1, 6)

print("CAN YOU GUESS MY NUMBER? (1-5)")
a = input("Enter your guess: ")

while a != n:
    if int(a) == n:
        print("Correct guess!")
        break;
    print('Try again!')
    a = input("Enter your guess: ")