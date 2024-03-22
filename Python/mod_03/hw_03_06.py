def format_string(string, length):
    if length <= len(str(string)):
        return(string)
    else:        
        return(" "*int(((int(length) - len(str(string)))//2)) + str(string))
    
#format_string(string='aaaaaaaaaaaaaaaaac', length=12)
#format_string(length=15, string='abaa')