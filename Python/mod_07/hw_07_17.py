#Повернемося до попереднього завдання та виконаємо зворотне. 
#Напишіть рекурсивну функцію encode для кодування списку або рядка. 
#Як аргумент функція приймає список ( наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]) або рядок (наприклад, "XXXZZXXYYYZZ").
#Функція повинна повернути закодований список елементів (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).


def encode(data):
    if len(data) == 0:
        return []
    for i in range(len(data)):
        if isinstance(data[i], str) and i+1 != len(data) and isinstance(data[i+1], str):
            past_list = [] if i==0 else data[:i]
            count = 0
            for j in data[i:]:
                if j == data[i]:
                    count += 1
                else:
                    break
            n = [data[i], count]
            n.extend(data[count+len(past_list):])
            past_list.extend(n)
            return encode(past_list)
        elif i == len(data)-1 and isinstance(data[i], int):
            return data