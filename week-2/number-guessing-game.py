numberToGuess = 5
attempts = 3;

print('Welcome to number guessing game');
print('Guess a number between 1 and 10');
print(f"You have {attempts} attempts left");

while attempts > 0:
    guess = input('Enter your guess: ');
    if not guess.isdigit():
        print('Please enter a valid number');
        continue;
    guess = int(guess);
    if guess == numberToGuess:
        print('You guessed it!');
        break;
    elif guess > numberToGuess:
        print('Too high');
    else:
        print('Too low');
    attempts -= 1;
    print(f"You have {attempts} attempts left");
    