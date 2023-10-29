# Task 2 
import random

# Task 1: Define the list of possible words
favourite_fruits = ["banana", "apple", "kiwi", "Mango", "Grapes"]
word_list = favourite_fruits
print(word_list)

# Task 2.2
word = random.choice(word_list)
print(f"The chosen fruit is: ", word)

# Task 3 
guess = input("Enter a single letter: ")

# Task 4 

if len(guess) == 1 and guess == str(guess):
    print("Good guess!")
else:
    print("Oops! That is not a valid input")


class hangman:
    def __init__(self,word_list,num_lives=5):
            self.word = random.choice(word_list)
            self.word_guessed = ['_' for _ in self.word]
            self.num_letters = len(set(self.word))
            self.num_lives = num_lives
            self.word_list = word_list
            self.list_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            for letter in word:
                if self.word[letter] == guess:
                    self.word_guessed[letter] = guess
            self.num_letter =- 1
        else:
            self.num_lives =- 1
            print(f"Sorry, {letter} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            print(f"Sorry, {guess} is not in the word. Try again.")
    
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ") 
            if not len(guess) == 1 and not guess.isalpha():
                print("Invalid letter. Please, entere a single alphabetical character.")
            elif guess in self.list_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_guesses.append(guess)
                print("Your valid guess is: ", guess)

    def play_game(self):
        num_lives = 5 
        hangman_game = hangman(word_list)
        while True:
            if self.num_lives == 0:
                print("You lost!")
            elif self.num_letters > 0:
                self.ask_for_input()
            else:
                print("Congratulations. You won the game")

favourite_fruits = ["banana", "apple", "kiwi", "Mango", "Grapes"]
word_list = favourite_fruits
hangman_game = hangman(word_list)
hangman_game.play_game()

