#Task 2 
import random

# Task 1: Define the list of possible words
favourite_fruits = ["banana", "apple", "kiwi", "Mango", "Grapes"]
word_list = favourite_fruits
print(word_list)

#Task 2.2
word = random.choice(word_list)
print(f"The chosen fruit is: ", word)

# Task 3 
guess = input("Enter a single letter: ")

# Task 4 
if len(guess) == 1 and guess == str(guess):
    print("Good guess!")
else:
    print("Oops! That is not a valid input")

