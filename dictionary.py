import json


dictionary = json.load(open("data.json"))

word = input("Enter word: ")
print(str(dictionary[word]))
