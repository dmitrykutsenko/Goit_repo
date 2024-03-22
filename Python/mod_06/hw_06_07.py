import re

def sanitize_file(source, output):

    # Use the context manager with to open the source file in read mode
    with open(source, "r") as source_file:

        # Read the content of the source file
        content = source_file.read()

        # Remove any numbers from the content using a regular expression
        content = re.sub(r"\d+", "", content)

        # Use the context manager with to open the output file in write mode
        with open(output, "w") as output_file:

            # Write the sanitized content to the output file
            output_file.write(content)

#This function will read the content of the source file using the with context manager and "r" mode. It will use a regular expression to remove any numbers from the content. It will write the new content of the output file cleaned of numbers using the context manager with and mode "w". It will write the new content of the output file in one go using the write method. However, it will not handle any errors or exceptions that may occur while opening or writing to the files. If you want to make your code more robust, you will need to add some error handling mechanisms.