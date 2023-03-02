import random
import os

number = random.randint(1, 100)
trials = 10

print ("Guessing Game!")

for count in range(trials):
    guess = int(input("Guess the number between 1 and 100: "))
    
    if guess == number:
        print("\nCongratulations!\nYou guessed the correct number in", count+1, "trials.\n")
        break
    elif guess < number:
        print("Your guess is too low. Try again.")
    elif guess > number:
        print("Your guess is too high. Try again.")
else:
    print("\nSorry, you have used all", trials, "trials. The correct number was", number)

os.system("pause")