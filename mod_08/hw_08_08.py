#Є список IP адрес:
#
#IP = [
#    "85.157.172.253",
#    ...
#]
#
#Реалізуйте дві функції. Перша get_count_visits_from_ip за допомогою Counter повертатиме словник, де ключ це IP, а значення – кількість входжень у вказаний список.
#
#Приклад:
#{
#    '85.157.172.253': 2,
#    ...
#}
#
#Друга функція get_frequent_visit_from_ip повертає кортеж з найбільш часто уживаним в списку IP і кількістю його появ в списку.
#
#Приклад:
#('66.50.38.43', 4)

# Import the Counter class from the collections module
from collections import Counter

# Define a function to get the count of visits from each IP
def get_count_visits_from_ip(ips):
    # Create a Counter object from the list of IPs
    counter = Counter(ips)
    # Convert the Counter object to a dictionary
    count_dict = dict(counter)
    # Return the dictionary
    return count_dict

# Define a function to get the most frequent visit from an IP
def get_frequent_visit_from_ip(ips):
    # Create a Counter object from the list of IPs
    counter = Counter(ips)
    # Get the most common IP and its count using the most_common method
    frequent_ip, frequent_count = counter.most_common(1)[0]
    # Return a tuple with the IP and its count
    return (frequent_ip, frequent_count)

#To test the functions, I used a sample list of IPs. Here are the results:

# Test the functions with a sample list of IPs
IP = [
    "85.157.172.253",
    "66.50.38.43",
    "66.50.38.43",
    "85.157.172.253",
    "66.50.38.43",
    "66.50.38.43",
]

print(get_count_visits_from_ip(IP)) # Output: {'85.157.172.253': 2, '66.50.38.43': 4}
print(get_frequent_visit_from_ip(IP)) # Output: ('66.50.38.43', 4)