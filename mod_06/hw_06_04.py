def add_employee_to_file(record, path):

    #Open the file in append mode
    file = open(path, "a")

    #Write the employee record to the file, followed by a newline
    file.write(record + "\n")

    # Close the file
    file.close()

# This function will add an employee (record parameter) in the form of a string such as "Drake Mikelsson,19" to the file (path parameter - the path to the file). It will open the file in append mode, so that the old information in the file is also preserved. It will write each record from a new line, as required. It will not use the context manager with. However, it will not handle any errors or exceptions that may occur while opening or writing to the file. If you want to make your code more robust, you will need to add some error handling mechanisms.