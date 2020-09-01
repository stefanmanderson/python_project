import random
n = random.randint(0, 3)

print(n)
print("CAN YOU GUESS MY NUMBER? (1-20)")
a = input("Enter your guess: ")

while a != n:
    if int(a) == n:
        print("Correct guess!")
        break;
    print('Try again!')
    a = input("Enter your guess: ")