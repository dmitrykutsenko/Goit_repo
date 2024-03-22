grades =  {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
descs =  {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough", "D": "Satisfactorily", "C": "Good", "B": "Very good", "A": "Perfectly"}

def get_grade(key):
    found = grades.get(str(key))
    if found:    
        print(str(found))


def get_description(key):
    found = descs.get(str(key))
    if found:    
        print(str(found))
        
get_grade("A")
get_description("A")