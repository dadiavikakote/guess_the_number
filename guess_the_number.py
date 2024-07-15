import random

range = input("Enter the range: ")

if range.isdigit():
    range = int(range)


    if range <= 0:
        print('please enter a number greater than 0.')
        quit()
else:
    print('Please enter a number.')
    quit()



random_number = random.randint(0, range)
guesses = 0

while True:
    guesses += 1
    player_guess = input("Make a guess: ")
    if player_guess.isdigit():
        player_guess = int(player_guess)
    else:
        print('Please enter a number.')
        continue


    if player_guess == random_number:
        print("You got it!")
        break
    elif player_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")


print("You guessed it in", guesses, "tries.")