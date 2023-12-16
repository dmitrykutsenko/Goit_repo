# import the re module for regular expressions
import re

# define the find_all_words function
def find_all_words(text, word):
    # create an empty list to store the matches
    matches = []
    # use the re.findall function to find all occurrences of the word in the text, ignoring the case
    # use the re.IGNORECASE flag to make the search case-insensitive
    results = re.findall(word, text, flags=re.IGNORECASE)
    # loop through the results and append them to the matches list
    for result in results:
        matches.append(result)
    
    # return the matches list
    return matches


print(find_all_words(
"Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
"Python"))

#This will print:
#['Python', 'Python']