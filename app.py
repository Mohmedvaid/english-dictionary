import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word.lower()
    if word in data:
        return data["word"]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        suggestion = get_close_matches(word, data.keys())[0]
        yn = input(
            f"Did you mean '{suggestion}'? Enter Y if yes, or N if no: ")
        if yn.upper() == "Y":
            return data[suggestion]
        elif yn.upper() == "N":
            return "This word does not exists in the dictionary."
        else:
            return "The input was not recognized."
    else:
        return "This word does not exists in the dictionary."


word = input("Enter a word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
