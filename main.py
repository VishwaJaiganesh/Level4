import random

num_of_guesses = 0
random_number = random.randint(1, 10)
users_guess = 0
while num_of_guesses < 7:
    user_guess = int(input("Guess a number between 1 and 10: "))
    num_of_guesses = num_of_guesses + 1
    if user_guess > 10 or users_guess > 1:
        print("IT CAN'T BE THAT NUMBER!")
    else:
        if user_guess > random_number:
            print("Lower!")
        elif user_guess < random_number:
            print("Higher!")
        elif user_guess == random_number:
            print("You got it! It took you " + str(num_of_guesses) + " guesses.")
            break

if num_of_guesses == 7:
    print("The secret number was " + str(random_number))
