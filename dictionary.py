import json


dictionary = json.load(open("data.json"))

def translate(word):
    return dictionary[word]

word = input("Enter word: ")

if word in dictionary:
    print(str(translate(word)))

else:
    print("{:s} is not a valid word !".format(word))
