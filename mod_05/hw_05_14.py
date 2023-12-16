import re

# define the find_all_phones function
def find_all_phones(text):
    # use the re.findall function to find all matches of the phone pattern in the text
    # the phone pattern consists of the following parts:
    # 1) the + symbol
    # 2) the digits 380
    # 3) the ( symbol
    # 4) two digits
    # 5) the ) symbol
    # 6) three digits
    # 7) the - symbol
    # 8) one or two digits
    # 9) the - symbol
    # 10) two or three digits
    # the phone pattern must have exactly 17 characters, so we use {n} to specify the number of repetitions for each part
    #by AI
    #result = re.findall(r"\+380\(\d{2}\)\d{3}-\d{1,2}-\d{2,3}", text)
    #by human
    result = re.findall(r"\+380\(\d{2}\)\d{3}-(?:\d{1}\-\d{3}|\d{2}-\d{2}){1}", text)
    #recommedation by course
    #result = re.findall(r"[a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-Z]{2,}", text)
    # return the result list
    return result

# You can test this function by calling it with different arguments and printing the output. For example:

print(find_all_phones("My phone number is +380(67)777-7-777 and yours is +380(50)123-45-67. What about +380(93)1111111? Is that a valid phone number?"))

# This will print:
#['+380(67)777-7-777', '+380(50)123-45-67']