import json


dictionary = json.load(open("data.json"))

# get answer from dictionary and give error if not found
def translate(word):
    if word in dictionary:
            return dictionary[word]

    else:
        print("{:s} is not a valid word. Please double check".format(word))

# convert word input to lowercase
def to_lower(word):
    return word.lower()

word = input("Enter word: ")

print(translate(to_lower(word)))
