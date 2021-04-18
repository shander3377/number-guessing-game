import random
number = random.randint(1, 9)
chances = 0
while chances<5:
    guess = int(input("Type your random guess: "))

    if(guess == number):
        print("Congratulations")
        chances=-1
        break
    elif guess > number:
                print("Your guess was too high guess a number less than " , guess)
                chances+=1
    else: 
                print("Your guess was too low guess a number more than " , guess)
                chances+=1
if not chances < 5:
    print("You lost. The number was " + number)