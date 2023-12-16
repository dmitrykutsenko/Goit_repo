def write_employees_to_file(employee_list, path):

    # Open the file in write mode
    file = open(path, "w")

    # Loop through the employee list
    for department in employee_list:

        # Loop through each department
        for employee in department:

            # Write the employee information to the file, followed by a newline
            file.write(employee + "\n")

    # Close the file
    file.close()

#This function will write the contents of employee_list to a file using "w" mode. It will not use the context manager with. It will write each employee's information from a new line, as required. However, it will not handle any errors or exceptions that may occur while opening or writing to the file. If you want to make your code more robust, you will need to add some error handling mechanisms.