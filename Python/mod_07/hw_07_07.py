def data_preparation(list_data):
    s =list()
    for i in list_data:
        if len(i)>2:
            i.remove(min(i))
            i.remove(max(i))
        s.extend(i)
    s1 = sorted(s, reverse=True)
    return s1
a = [[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]
print(data_preparation(a))