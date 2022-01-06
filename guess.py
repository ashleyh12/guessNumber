import random  #package that comes with python where certain functions are available in file

def guess(x):
  random_number = random.randint(1, x) #random number between 1 and x 
  guess = 0
  while guess != random_number:
    guess = int(input(f'Guess a number between 1 and {x}: ')) #keep getting the user's guess number until the random number is correct
    if guess < random_number:
      print("Sorry, guess again. Too low.")
    elif guess > random_number:
      print("Sorry, guess again. Too high.")
  print(f"Congrats! You guessed the number {random_number}")

(guess(1000))


