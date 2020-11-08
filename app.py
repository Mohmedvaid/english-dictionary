import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word.lower()
    if word in data:
        return data["word"]
    elif len(get_close_matches(word, data.keys())) > 0:
        return f"Did you mean '{get_close_matches(word, data.keys())[0]}'?"
    else:
        return "This word does not exists in the dictionary."

word = input("Enter a word: ")
print(translate(word))