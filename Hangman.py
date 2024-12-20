'''Implement your solution in this file.
Make sure that you decompose your solution into appropriate 
functions and that you include appropriate documentation.'''
import random
import string

def load_words():
  
    try:
        with open("words.txt", "r") as file:
            word_list = file.read().split()
        return word_list
    except FileNotFoundError:
        print("Error: 'words.txt' file not found.")
        return []

def choose_word(word_list):
    return random.choice(word_list) if word_list else ""

def hangman():
    word_list = load_words()
    
    if not word_list:
        return  
    
    secret_word = choose_word(word_list).lower()
    unique_letters = set(secret_word)
    
    guesses_remaining = 10
    warnings_remaining = 3
    letters_guessed = set()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    
    while guesses_remaining > 0:
        print("-" * 20)
        print(f"Guesses remaining: {guesses_remaining}")
        print(f"Warnings remaining: {warnings_remaining}")
        print("Letters not yet guessed:", ''.join(sorted(set(string.ascii_lowercase) - letters_guessed)))
        
        guessed_word = ''.join([char if char in letters_guessed else '-' for char in secret_word])
        print(f"Current word: {guessed_word}")
        
        if unique_letters <= letters_guessed:
            print(f"Congratulations, you guessed the word: {secret_word}!")
            score = guesses_remaining * len(unique_letters)
            print(f"Your score is: {score}")
            return
        
        guess = input("Please guess a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Invalid input! You have {warnings_remaining} warnings left.")
            else:
                guesses_remaining -= 1
                print(f"Invalid input! You lost a guess. Guesses remaining: {guesses_remaining}")
            continue
        
        if guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"You've already guessed that letter! Warnings left: {warnings_remaining}")
            else:
                guesses_remaining -= 1
                print(f"You've already guessed that letter! Guesses remaining: {guesses_remaining}")
            continue
        
        letters_guessed.add(guess)
        
        if guess in secret_word:
            print(f"Good guess: {guessed_word}")
        else:
            if guess in vowels:
                guesses_remaining -= 2
                print(f"The letter '{guess}' is not in the word. You lost 2 guesses.")
            else:
                guesses_remaining -= 1
                print(f"The letter '{guess}' is not in the word. You lost 1 guess.")
        
    print(f"Sorry, you've run out of guesses. The word was: {secret_word}. Better luck next time!")

hangman()
