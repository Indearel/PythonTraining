import random

roll = random.randint(1,6)

#print("The computer rolled a " + str(roll))

guess = int(input('Guess the dice roll: \n'))

if guess == roll:
    print("Correct, you`ve predicted correct result ! \nThe roll is a " + str(roll))
else: 
    print("Your prediction is incorrect :( \nThe roll is " + str(roll))
