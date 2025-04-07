"""
Number Guessing Game Challenge

Create a number guessing game where the program generates a random 
4-digit number that ALL THE DIGITS SHOULD BE UNIQUE and the player guesses. 
After each guess, the program tells you how many digits are correct

A correct digit is both the SAME NUMBER in the SAME POSITION

Ask the player to guess until all 4 digits are correct, then end the game

(Note: numbers can start with 0) 

Example 1:
secret: 1234
guess:  1234
Result: 4


Example 2
secret: 0534
guess:  1269
Result: 0
guess:  0234
Result: 2
guess:  0534
Result: 4

Example 3:
secret: 1234
guess:  1972
Result: 1

"""

import random


def generate_secret():
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    if num2 == num1:
        while num2 == num1:
            num2 = random.randint(0,9)
    num3 = random.randint(0,9)
    if num3 == num2 or num3 == num1:
        while num3 == num2 or num3 == num1:
            num3 = random.randint(0,9)
    num4 = random.randint(0,9)
    if num4 == num3 or num4 == num3 or num4 == num2 or num4 == num1:
        while num4 == num3 or num4 == num3 or num4 == num2 or num4 == num1:
            num4 = random.randint(0,9)
                
    secret = f"{num1}{num2}{num3}{num4}"
    return secret
    
## Look at how I can do this with the sample() function that Sam was discussing

    """
    Generate a random 4-digit number where digits are DISTINCT
    0000 9999 1020 ARE NOT VALID
    Hint: To generate numbers use random.randint()
    Hint2: Digits can start with 0
    Returns: string of 4 digits
    """
    

def check_guess(secret, guess):
    """
    Compare the guess with the secret number
    Returns: correct number of digits
    """
    correct_digits = 0

    s = str(secret)
    g = str(guess)
    # What I learned is that the len() function doesn't work on int.. strings, tuples, etc
    
    for i in range(4):
        if s[i] == g[i]:
            correct_digits += 1
    
    return correct_digits


def play_game():
    secret_num = generate_secret()
    
    while True:
        guess = input('Make a guess: ')
        
        correct_digits = check_guess(secret_num, guess)

        print('Result: ', correct_digits)
        if correct_digits == 4:
            break

    """
    Main game loop:
    - Get the secret number
    - Handle player turns
    - Show results after each guess
    - End game when someone wins
    """

    

if __name__ == "__main__":
    play_game()