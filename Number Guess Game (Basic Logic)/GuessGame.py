#Number guess game
import random
Number=random.randint(1,100)
print("You have 10 chances to guess the chosen number from 1 to 100:")
no_of_guesses=0
while no_of_guesses<=10:
    guess=int(input("Enter your guess:"))
    if guess==Number:
        print("Your Guess is right")
        break
    elif guess>Number:
        print("Too high! try again")
    elif guess<Number:
        print("Too low! try again")
    no_of_guesses+=1
else:
    print("Game Over! The Number was", Number)