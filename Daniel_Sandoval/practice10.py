# Write a program that reads a string and returns a table of the letters of the alphabet
# in alphabetical order which occur in the string together with the number of times each letter occurs.
# Case should be ignored. A sample output of the program when the user enters the data
# ThiS is String with Upper and lower case Letters, would look this this =>


def cont_character_alphabet(string_word):
    character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    string_character = list(string_word.lower())
    accountant = 0
    for i in range(0, character.__len__()):
        for j in range(0, string_character.__len__()):
            if string_character[j] == character[i]:
                accountant += 1
        if accountant != 0:
            print character[i] + " - " + str(accountant);
        accountant = 0


enter_word = raw_input("Enter the text to be read: ")

cont_character_alphabet(enter_word)