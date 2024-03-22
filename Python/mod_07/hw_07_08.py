def token_parser(s):
    final_list = list()
    numbers = ""
    if len(s) == 0:
        return list()
    if s[-1].isdigit():
        n = s[::-1]
        num = ""
        a = 0
        while n[a].isdigit():
            num += n[a]
            a +=1
        num = num[::-1]
    for i in s:
        if i.isdigit():
            numbers += i
        elif i in"+-/*)":
            final_list.append(numbers)
            final_list.append(i)
            numbers = ""    
        elif i in "()":
            final_list.append(i)
    if num != "":
        final_list.append(num)
    f_l = list(filter(lambda el: el != "", final_list))
    return f_l