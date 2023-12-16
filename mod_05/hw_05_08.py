grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

def formatted_grades(students):
    res = []
    i = 0
    #for el in formatted_grades(students):
    for name, grade in students.items():
        marks = {}
        # Loop through the students dictionary and get the corresponding grade value from the grades dictionary
        for name, grade in students.items():
        # Get the numeric mark value from the grades dictionary using the grade as the key
            mark = grades[grade]
            # Store the name and mark pair in the marks dictionary
            marks[name] = mark
        
            res.append(str(f"{(i+1):>4}")+"|"+str(f"{name:<10}")+"|"+str(f"{grade:^5}")+"|"+str(f"{marks.get(name):^5}"))
            
            i += 1
            if i == 4:
               return res
    

for el in formatted_grades(students):
        print(el)

#formatted_grades(students)
