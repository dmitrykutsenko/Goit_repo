source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

def save_applicant_data(source, output):

    # Use the context manager with to open the output file in write mode
    with open(output, "w") as output_file:

        # Loop through the source list
        for applicant in source:

        # Get the name, specialty, and scores of the applicant
            name = applicant["name"]
            specialty = applicant["specialty"]
            math = applicant["math"]
            lang = applicant["lang"]
            eng = applicant["eng"]

            # Create a string with the applicant data, separated by commas
            data = f"{name},{specialty},{math},{lang},{eng}\n"

            # Write the data to the output file
            output_file.write(data)
    #print(data)

#save_applicant_data(source, output)
#save_applicant_data(source)
    
# This function will save the specified list from the source parameter to a file from the output parameter. It will use the context manager with to open and close the output file automatically. It will loop through the source list and get the name, specialty, and scores of each applicant. It will create a string with the applicant data, separated by commas, and write it to the output file. It will write the new contents of the output file using the write method. However, it will not handle any errors or exceptions that may occur while opening or writing to the file. If you want to make your code more robust, you will need to add some error handling mechanisms.