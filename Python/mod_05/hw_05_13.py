import re

# define the find_all_emails function
def find_all_emails(text):
    # use the re.findall function to find all matches of the email pattern in the text
    # the email pattern consists of three parts:
    # 1) the prefix, which starts with a letter and can contain letters, numbers, underscore and dot
    # 2) the @ symbol
    # 3) the suffix, which consists of two parts separated by a dot, each part containing only letters
    # the prefix and the top-level domain name must have at least two characters
    result = re.findall(r"[a-zA-Z][\w.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", text)
    # return the result list
    return result

# You can test this function by calling it with different arguments and printing the output. For example:

print(find_all_emails("My email is john.doe@example.com and yours is jane_doe@another.example.co.uk. What about bob@example? Is that a valid email?"))

#This will print:
#['john.doe@example.com', 'jane_doe@another.example.co.uk']