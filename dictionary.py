import json


dictionary = json.load(open("data.json"))

def translate(word):
    return dictionary[word]

word = input("Enter word: ")

print(str(translate(word)))
