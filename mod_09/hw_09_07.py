'''
Потрібно розвьязати наступну задачку на пайтоні. Є список name з іменами користувачів, але всі починаються з малої літери.

name = ["dan", "jane", "steve", "mike"]

Розробіть функцію normal_name, яка приймає список імен та повертає теж список імен, але вже з правильними іменами з великої літери.

['Dan', 'Jane', 'Steve', 'Mike']

Необхідно використовувати функцію map. Не забудьте, що необхідно виконати перетворення типів для map.
'''

def normal_name(name_list):
    # Use map to capitalize each name in the list
    capitalized_names = list(map(str.capitalize, name_list))
    return capitalized_names

# Example usage:
names = ["dan", "jane", "steve", "mike"]
result = normal_name(names)

print(result)