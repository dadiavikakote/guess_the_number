import random

# It asks the user to enter a range of numbers in which to guess the number
range = input("Enter the range: ")

# Check if the input is a digit
if range.isdigit():
    range = int(range)

    # Check if the entered range is greater than 0
    if range <= 0:
        print('Please enter a number greater than 0.')
        quit()
else:
    # If input is not a digit, prompt the user to enter a number and exit
    print('Please enter a number.')
    quit()

# Generate a random number within the given range
random_number = random.randint(0, range)
# Initialize the number of guesses
guesses = 0

# Start an infinite loop for guessing
while True:
    # Increment the number of guesses
    guesses += 1
    # Prompt the user to make a guess
    player_guess = input("Make a guess: ")

    # Check if the guess is a digit
    if player_guess.isdigit():
        player_guess = int(player_guess)
    else:
        # If the guess is not a digit, prompt the user to enter a number
        print('Please enter a number.')
        continue

    # Check if the player's guess is correct
    if player_guess == random_number:
        print("You got it!")
        break
    elif player_guess > random_number:
        # If the guess is higher than the random number
        print("You were above the number!")
    else:
        # If the guess is lower than the random number
        print("You were below the number!")

# Print the total number of guesses
print("You guessed it in", guesses, "tries.")
