print("This is a random number guessing game \n be ready ")
print("You have to guess the number between 1 and 50")
random_number = 34 
print("you have 5 lives left good luck")
lives = 5
x = int(input("Please enter your 1st guess"))
if x > random_number :
    print("you are making a bigger guess")
if x < random_number :
    print("The number is smaller than your guess")
if x == random_number:
    print("your guess was right!")
else :
    lives = lives - 1
    print(f"you have {lives} lives remeinging")
y = int(input("Please enter your 2nd guess"))
if y > random_number :
    print("you are making a bigger guess")
if y < random_number :
    print("The number is smaller than your guess")
if y == random_number:
    print("your guess was right!")
else :
    lives = lives - 1
    print(f"you have {lives} lives remeinging")
z = int(input("Please enter your 3rd guess"))
if z > random_number :
    print("you are making a bigger guess")
if z < random_number :
    print("The number is smaller than your guess")
if z == random_number:
    print("your guess was right!")
else :
    lives = lives - 1
    print(f"you have {lives} lives remeinging")
a = int(input("Please enter your 3rd guess"))
if a > random_number :
    print("you are making a bigger guess")
if a < random_number :
    print("The number is smaller than your guess")
if a == random_number:
    print("your guess was right!")
else :
    lives = lives - 1
    print(f"you have {lives} lives remeinging")
b = int(input("Please enter your 3rd guess"))
if b > random_number :
    print("you are making a bigger guess")
if b < random_number :
    print("The number is smaller than your guess")
if b == random_number:
    print("your guess was right!")
else :
    lives = lives - 1
    print(f"you have {lives} lives remeinging")
print(f"your guesses were {x},{y},{z},{a},{b}")
print (f"random number was {random_number}")






    




