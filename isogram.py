# an isogram is a word where the string has no repeating letters,
# whether consecutively or non-consecutiively.
# i.e. 'cat', or 'isogram' are isograms, but 'animal' is not
# make a program that calculates if a word is an isogram or not.

import collections


def is_isogram(string):
    # split
    # compare
    string = collections.Counter(string)
    for x, y in string.items():
        if y > 1:
            return "this is not an isogram! try again (or quit, idk that's up to you)."
        else:
            return "this works, this is an isogram!"


while True:
    word = input("enter a word to see if it is an isogram or not (type 'end' to end): ")
    if word.lower() == "end":
        print("bye!")
        break
    print(is_isogram(word))
