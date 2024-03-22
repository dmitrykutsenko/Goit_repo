# Define a function that returns a list of formatted strings
def formatted_numbers():
    # Create an empty list to store the formatted strings
    result = []
    # Add the header row to the list, using the center alignment (^) and the width (10) for each column
    result.append("|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary"))
    # Loop through the numbers from 0 to 15
    for num in range(16):
        # Convert the number to hexadecimal using the hex() function and remove the '0x' prefix
        hex_num = hex(num)[2:]
        # Convert the number to binary using the bin() function and remove the '0b' prefix
        bin_num = bin(num)[2:]
        # Add the formatted row to the list, using the left alignment (<), center alignment (^), and right alignment (>) for each column
        result.append("|{:<10}|{:^10}|{:>10}|".format(num, hex_num, bin_num))
    # Return the list of formatted strings
    return result

# Call the function and print each element in the list
for el in formatted_numbers():
    print(el)