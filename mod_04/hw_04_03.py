def format_ingredients(items):
    res = ""
    for each in items:
        if each == items[0]:
            res = str(each)
        elif each == items[-1]:
            res = res + " and " + str(each)
        else:
            res = res + ", " + each
    
    print(str(res))


format_ingredients( ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] )