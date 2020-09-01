import random
n = random.randint(1, 6)

print("CAN YOU GUESS MY NUMBER? (1-5)")
print("YOU ONLY HAVE 3 ATTEMPTS TO GUESS MY NUMBER! USE IT WISELY!")
a = input("Enter your guess: ")
trial = 1

while a != n:
    if int(a) == n:
        print("Correct guess!")
        break;
    if trial == 3:
        break;
    print('Try again!')
    trial += 1
    print("Number of trials : " + str(trial) + "/3")
    a = input("Enter your guess: ")