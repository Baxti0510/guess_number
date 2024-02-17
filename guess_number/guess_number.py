import random

top_of_range = input("Enter a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next line.")
        quit()
else:
    print("Please type a number next time.")
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Enter your guess number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number")
        continue

    if user_guess == random_number:
        print("Congratulations! You found it")
        break
    elif user_guess > random_number:
        print("Your guess is above the number")
    else:
        print("Your guess is below the number")

print("You got it in " + str(guesses) + " guesses")