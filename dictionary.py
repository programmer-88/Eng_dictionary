import json


dictionary = json.load(open("data.json"))

def translate(word):
    if word in dictionary:
            return dictionary[word]

    else:
        print("{:s} is not a valid word !".format(word))

word = input("Enter word: ")

print(translate(word))
