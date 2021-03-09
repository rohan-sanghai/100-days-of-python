#Step 1 
import random 
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
display= [] 
for i in chosen_word:
  display += "_"
print(display)
guess = input("Enter a letter ")
guess= guess.lower()
def split(chosen_word):
    return [char for char in chosen_word]
for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter 
print(display)


