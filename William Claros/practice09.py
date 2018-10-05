# Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:
from string import replace

def replace_word(string, old, new):
    return replace(string, old, new)

string = raw_input("Enter a text: ")
character1 = raw_input("Enter a character or word from the previous text: ")
character2 = raw_input("Enter a character or word with which the text will be replaced: ")

print (replace(string, character1, character2))
