import json
# Library that compares text
# SequenceMatcher
# from difflib import SequenceMatcher
# SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(w, data.keys())) >0:
        yn = input("Did you mean %s instead? Enter y if yes, or n if no." % get_close_matches(word, data.keys())[0])
        yn= upper(yn)
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your entry."
#        r_yes_no = yes_now.lower()
#        if r_yes_no != "y" || "n":
#            return "Invalid input, please try again"
#        elif r_yes_no = "y":
#            translate(word)
#        elif r_yes_no = "n":
#            translate(word)
    else:
        return "The word doesn't exist. Please double check it"

word = input("Enter word: ")

output  translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
