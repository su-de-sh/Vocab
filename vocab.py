import json
from difflib import get_close_matches

data = json.load(open('data.json'))


your_word = input("Enter your word:").lower()


def WordMeaning(word):
    if your_word in data:
        return data[word]

    
    elif len(get_close_matches(your_word,data.keys()))>0:
        query = input("Did you mean {} instead?".format(get_close_matches(your_word,data.keys())[0]))
        if query == "Y":
            return data[get_close_matches(your_word,data.keys())[0]]
        elif query == "N":
            return "Meaning not found"
    else:
        return ' Meaning not found '

meaning = WordMeaning(your_word)
print(meaning)