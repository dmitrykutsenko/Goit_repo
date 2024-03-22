def read_employees_from_file(path):

    #Initialize the employee list as empty
    employee_list = []

    #Open the file in read mode
    file = open(path, "r")

    #Loop until the end of the file
    while True:

        #Read one line from the file
        line = file.readline()

        #If the line is empty, break the loop
        if not line:
            break

        #Remove the newline character from the line
        line = line.strip()

        #Add the line to the employee list
        employee_list.append(line)

    #Close the file
    file.close()

    #Return the employee list
    return employee_list

    #This function will read data from a file using "r" mode. It will not use the context manager with. It will return a list of employees from the file, as required. It will take into account the presence of the end-of-line character \n when reading data from the file, so it will remove it when adding the read line to the list. However, it will not handle any errors or exceptions that may occur while opening or reading the file. If you want to make your code more robust, you will need to add some error handling mechanisms