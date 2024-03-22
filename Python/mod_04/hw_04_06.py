def split_list(grade):
    list_below = list()
    list_above = list()
    
    if len(grade) > 0:
        sum = 0
        for i in grade:
            sum = sum + i
        aver = sum / len(grade)
        
        for i in grade:
            if i<= aver:
                list_below.append(i)
            else:
                list_above.append(i)
            
    res_tuple = (list_below, list_above)
    
    return(res_tuple)