#Number Guessing Game Objectives:
import random
from art import logo
from art import winner
print(logo)
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
print("\n##### Welcome to number guessing game #####")
print("The number I'm thinking is between 1 and 100....")
HARD_STEPS = 5
EASY_STEPS = 10
#Number that we need to guess
NO_GUESS = random.randint(1,100)
print(f"Douzzo the number is: {NO_GUESS}")

def check_answer(answer,guess,is_guess):
    if guess > answer:
        print(" Your Guess is too high.")
    elif guess < answer:
        print(" Your Guess is too low.")
    else:
        is_guess = True
    return is_guess

difficulity_level = input("Choose a difficulity level 'hard' or 'easy'! : ").lower()

if difficulity_level == "easy":
    no_of_steps = EASY_STEPS
    is_guess_right = False 
    while no_of_steps > 0 and is_guess_right == False:
        print(f"You have {no_of_steps} attempts left.") 
        guessed_number = int(input("Guess the number: "))
        is_guess_right = check_answer(NO_GUESS , guessed_number, is_guess_right)
        no_of_steps -= 1
elif difficulity_level == "hard" :
    no_of_steps = HARD_STEPS
    is_guess_right = False
    while no_of_steps > 0 and is_guess_right == False:
        print(f"You have {no_of_steps} attempts left.") 
        guessed_number = int(input("Guess the number: "))
        is_guess_right = check_answer(NO_GUESS , guessed_number, is_guess_right)
        no_of_steps -= 1       
else:
    print("You have entered a invalid difficulity level.")

if not is_guess_right:
    print("You have exhausted all attempts!.You lose!")
else:
    print(f"You have made the correct guess: {guessed_number}\n")
    print(winner)