import re

# define the replace_spam_words function
def replace_spam_words(text, spam_words):
    # create an empty string to store the result
    result = ""
    # loop through the spam words list
    for spam_word in spam_words:
        # use the re.sub function to replace the spam word with asterisks, ignoring the case
        # use the re.IGNORECASE flag to make the replacement case-insensitive
        # use the len function to get the length of the spam word and multiply it by '*'
        text = re.sub(spam_word, '*' * len(spam_word), text, flags=re.IGNORECASE)
        # assign the text to the result
    result = text
    # return the result
    return result

# You can test this function by calling it with different arguments and printing the output. For example:

print(replace_spam_words("This is a very bad sentence with some nasty words like crap and damn.",
["bad", "nasty", "crap", "damn"]))

#This will print:
# This is a very *[** sentence with some **](https://www.bing.com/search?form=SKPBOT&q=%20sentence%20with%20some%20)*[** words like **](https://www.bing.com/search?form=SKPBOT&q=%20words%20like%20)[** and **](https://www.bing.com/search?form=SKPBOT&q=%20and%20)**.