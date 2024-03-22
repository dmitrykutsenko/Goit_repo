def is_spam_words(text, spam_words, space_around=False):
    spam = False
    txt = text.lower().replace(".","")
    words_from_text = txt.split(" ")
    
    for each_spam in spam_words:

        if text.find(each_spam.lower()) and space_around==False:
            spam = True
            break
        for each_text in words_from_text:

            if space_around==False:
                if each_spam.lower() == each_text:
                    spam = True
                    break
            else:
                if each_spam.lower() == each_text.strip():
                    spam = True
                    break
    return spam

print("1", is_spam_words('Ты хорош, но выглядишь как лох.', ['лох'],True)) # True
print("2", is_spam_words("У діда в руках молоток.", ["лоток"]))  # True
print("3", is_spam_words("У діда в руках молоток.", ["лоток"], True))  # False
print("4", is_spam_words("У кота порожній лоток.", ["лоток"]))  # True
print("5", is_spam_words("У кота порожній лоток.", ["лоток"], True))  # True    
