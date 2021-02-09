# Hangman game!
# Assume the answer is "hangman"

from random import choice
A = ['h', 'a', 'n', 'g', 'm', 'a', 'n']

L = ['_', '_', '_', '_', '_', '_', '_']

words =choice(["Waffles","hangman","chicken","oranges"])

guess =''
count=0
badGuess=0

play = True
while count < 7 and badGuess < 6:
    # Ask the user to guess a letter
    letter = str(input("Guess a letter: "))
    guess += letter
    count = count + 1

    if letter not in words:
     badGuess = badGuess + 1
     print("BAD GUESS")
    print(badGuess)
    # Check to see if that letter is in the Answer
    i = 0
    for currentletter in words:

    # If the letter the user guessed is found in the answer, # set the underscore in the user's answer to that letter
        if letter == currentletter:
            L[i] = letter

        i = i + 1


# Display what the player has thus far (L) with a space # separating each letter
print(' '.join(str(n) for n in L))

# Test to see if the word has been successfully completed, # and if so, end the loop
if guess == words:
    print("GREAT JOB!")
else:
    print("YOU LOSE")
