# import the re module for regular expressions
import re

# define the find_word function
def find_word(text, word):
    # create an empty dictionary to store the result
    result = {}
    # use the re.search function to find the word in the text
    match = re.search(word, text)
    # if there is a match, set the result values accordingly
    if match:
        result['result'] = True
        result['first_index'] = match.start()
        result['last_index'] = match.end()
        result['search_string'] = match.group()
        result['string'] = text
# if there is no match, set the result values to None or False
    else:
        result['result'] = False
        result['first_index'] = None
        result['last_index'] = None
        result['search_string'] = word
        result['string'] = text
    
    # return the result dictionary
    return result


# You can test this function by calling it with different arguments and printing the output. For example:

print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "Python"))

#This will print:
#{
#'result': True,
#'first_index': 34,
#'last_index': 40,
#'search_string': 'Python',
#'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
#}