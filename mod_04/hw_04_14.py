import sys
#print(sys.argv)  

def parse_args():  
    result = ""
    i = 0
    for arg in sys.argv:
        if i >= 1: 
            print(i, arg)
            result = result + " " + arg
        i += 1                      
    print(result.lstrip())    
    return result.lstrip()

parse_args()
