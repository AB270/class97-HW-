#Number Guessing Game

from random import randint
guessesTaken = 0  
print('What is your name?')
myName = input()  
number = randint(1, 10) 
print('Hello, ' + myName + ', I am thinking of a number between 1 and 10')
while guessesTaken < 5:  
  print('Take a guess')
  guess = int(input())  
  guessesTaken = guessesTaken + 1  

  if number > guess:
    print('Guess is too low. Try again')
  if guess > number:
    print('Guess is too high. Try again')
  if guess == number:
    break


if guess == number:
  guessesTaken = str(guessesTaken)
  print('Good job, ' + myName + '! You guessed the correct number in ' + guessesTaken + ' guesses!')


if guess != number:
  number = str(number)
  print('Sorry...You ran out of guesses! ')