#number guessing game
import random

print('hello. who are you?')
name = input()

print('well, '+ name + " I'm thinking of a number between 1 and 10 bajillion")
secretNumber = random.randint(1,100)

for guessesTaken in range(1,10):
    print('take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break

if guess == secretNumber:
    print(name + 'guessed it in ' + str(guessesTaken) + ' guesses!')
else: 
    print('FAIL! ' + 'the correct number is ' + str(secretNumber))

