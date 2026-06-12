import random

# Generate random number
secret_number = random.randint(1, 100)

max_attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

else:
    print("\nGame Over!")
    print("The correct number was:", secret_number)