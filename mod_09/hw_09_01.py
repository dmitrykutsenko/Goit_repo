'''
For the problem about the evaluation system at the university
we have the following Python code:

def get_grade(key):
     grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
     return grade.get(key, None)

def get_description(key):
     description = {
         "A": "Perfectly",
         "B": "Very good",
         "C": "Good",
         "D": "Satisfactorily",
         "E": "Enough",
         "FX": "Unsatisfactorily",
         "F": "Unsatisfactorily",
     }
     return description.get(key, None)


def get_student_grade(option):   

Two functions were implemented in this code.
The first - get_grade, takes the key in the ECTS grade and returns the corresponding five-point grade (the first column of the table).
The second - get_description, also accepts the key in ECTS grades, but returns the explanation of the grade in text format (the last column of the table). Functions must return None for a non-existent key.

It is necessary to implement the higher-order function get_student_grade, which accepts the option parameter. 
If it is equal to "grade", then the function returns the get_grade function, and if its value is "description", then it returns the get_description function. 
If the value of the parameter did not match the specified values, the get_student_grade function should return None.
'''

def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)

def get_description(key):
    description = {
        "A": "Perfectly",
        "B": "Very good",
        "C": "Good",
        "D": "Satisfactorily",
        "E": "Enough",
        "FX": "Unsatisfactorily",
        "F": "Unsatisfactorily",
    }
    return description.get(key, None)

def get_student_grade(option):
    if option == "grade":
        return get_grade
        print(get_grade)
    elif option == "description":
        #return get_description
        print(get_description)
    else:
        #return None
        print(None)
    

get_student_grade('description')