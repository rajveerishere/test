
import random
print("guess the number between 1 to 50")
print("you have 5 lives to guess the number")
number = random.randint(1, 50)
def input_guess():
    guess = int(input("Enter your guess: "))
    return guess
def guess():
    lives = 5
    while lives > 0:
        guess = input_guess()
        if guess == number:
            print("Congratulations! You guessed the number.")
            return
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        lives -= 1
        print(f"You have {lives} lives remaining.")
    print("Sorry, you ran out of lives. The number was:", number)
input_guess()
guess()
print(f"the number was {number}")