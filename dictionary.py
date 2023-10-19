import json
from difflib import get_close_matches

dictionary = json.load(open("data.json"))

# get answer from dictionary and give error if not found
def translate(word):
    word = word.lower()
    if word in dictionary:
            return dictionary[word]

    else:
        return get_closest(word)
    
# chexk if there is a word that nearly matches
def get_closest(word):
    close_match = get_close_matches(word, dictionary.keys(), cutoff = 0.8)
    
    if close_match:
        close_match = close_match[0]
        confirmation = input("Did you mean {:s} instead? Enter Y if yes or N if no: ".format(close_match))

        if confirmation.lower() == "y":
            return dictionary[close_match]
        
        elif confirmation.lower() == "n":
             return "{:s} does not exist. Please double check it.".format(word)
        
        else:
             return "{:s} does not exist. Please double check it.".format(word)

    else:
         return "{:s} does not exist. Please double check it.".format(word)
word = input("Enter word: ")

print(translate(word))
