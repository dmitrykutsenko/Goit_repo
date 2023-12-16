# у нас є список із повторюваними спостереженнями якоїсь величини, вона може приймати значення X, Y або Z. Значення з'являються у довільному порядку та зберігаємо ми їх у списку ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"] або рядку "XXXZZXXYYYZZ".
#
# Внаслідок чого ми можемо зменшити обсяг інформації, що зберігається? Стиснення можна досягти заміною групи повторюваних значень на одноразове значення та лічильник повторів: ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
#
# Напишіть рекурсивну функцію decode для декодування списку, закодованого цим способом. Як аргумент функція приймає закодований список. Функція має повернути розшифрований список елементів.

# write a recursive function that can decode a list encoded with a simple series-based technique. Here is the code I wrote:

# Define a recursive function to decode a list
# Also need to add a condition to check if the data has at least two elements left before repeating the second element. Here is the corrected code:

# forgot to convert the number element to an integer before repeating the second element. In Python, if you multiply a string by a string, you get a concatenation of the two strings. For example, 'X' * '3' gives 'X3', not 'XXX'.
# To fix this, I need to use the int() function to convert the number element to an integer before repeating the second element. Here is the corrected code:

#the problem is that I assumed that the data is a list of strings and integers, but it is actually a string of characters. Therefore, when I check if the first element is a number, I should use the isdigit() method instead of the isinstance() function. Also, when I slice the data, I should use single brackets instead of double brackets.
#To fix this, I need to modify my code as follows:

#handle the case when the data is an empty string. In that case, the function should return an empty list, not an empty string.
#To fix this, I need to add a condition to check if the data is an empty string and return an empty list accordingly. Here is the corrected code:

#handle the case when the data is a list of integers, not a string of characters. In that case, the function should use the isinstance() function instead of the isdigit() method to check if the first element is a number. Also, when I append the elements to the result, I should use brackets instead of quotes to create a list, not a string.
#To fix this, I need to modify my code as follows:

# Define a recursive function to decode a list
def decode(data):
    if len(data) == 0:
        return []
    elif len(data) == 1:
        return data
    else:
        if isinstance(data[0], str) and isinstance(data[1], int):
            return [data[0]] * data[1] + decode(data[2:])
        else:
            return [data[0]] + decode(data[1:])
    
decode(['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2])