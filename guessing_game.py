import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

MAX_GUESSES = 10

# Keep the game running until the user guesses the correct number or runs out of guesses
guesses = 0
while guesses < MAX_GUESSES:
    # Get the user's guess
    try:
        guess = int(input('Guess a number between 1 and 100: '))
    except:
        print('Invalid input! Please enter a number between 1 and 100.')
        continue

    # Check if the guess is too high, too low, or correct
    if guess > secret_number:
        print('Too high! Guess again.')
    elif guess < secret_number:
        print('Too low! Guess again.')
    else:
        print('Correct! You win!')
        break

    # Increment the number of guesses
    guesses += 1

if guesses == MAX_GUESSES:
    print('Sorry, you ran out of guesses. The secret number was', secret_number)
