import re

# define the find_all_links function
def find_all_links(text):
    # create an empty list to store the result
    result = []
    # use the re.finditer function to find all matches of the link pattern in the text
    # the link pattern consists of the following parts:
    # 1) the http:// or https:// prefix
    # 2) the domain name, which is a set of letters, numbers, underscores and dots
    # 3) the optional path, which starts with a slash and can contain any characters except spaces
    # we use the | operator to indicate alternatives for the prefix
    # we use the + operator to indicate one or more repetitions for the domain name and path
    # we use the \ character to escape special characters like . and /
    # we use the [^ ] character class to indicate any character except space
    # we add a condition to exclude domain names that have two consecutive dots, using a negative lookahead (?!\.)
    iterator = re.finditer(r"(http://|https://)[\w.]+(?!\.)(/[^\s]*)?", text)
    #iterator = re.finditer(r"[A-Za-z]{a}[\w.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", text) 

    # loop through the iterator and append each match to the result list
    for match in iterator:
        if str(match).find("..")==-1:
            result.append(match.group())
    # return the result list
    return result

#You can test this function by calling it with different arguments and printing the output. For example:
print(find_all_links("The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com "))

# This will print:
#['https://www.google.com', 'https://www.facebook.com', 'http://github.com']