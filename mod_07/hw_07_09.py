# Напишіть функцію all_sub_lists, що повертає список, який містить всі можливі підсписки заданого.

# Наприклад, якщо функції передано аргумент список [1, 2, 3], то функція має повернути наступний список: [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]].

# Функція all_sub_lists повинна повертати щонайменше один список з порожнім підсписком [[]].

def all_sub_lists(data):
    final_list = list()
    final_list.append([])
    for i in range(len(data)):
        for j in range(i+1, len(data)+1):
            final_list.append(data[i:j])
    return list(sorted(final_list, key=lambda n:len(n)))