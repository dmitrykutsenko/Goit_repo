# write a Python function that will convert the date from the database in ISO format '2021-05-27 17:08:34.149Z' into the following string
#'Thursday 27 May 2021' - day of the week, number, month and year. The converted value is returned by the function during the call.

# Import the datetime module
from datetime import datetime

def get_str_date(date):
    # Convert the ISO format string to a datetime object
    datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')

    # Format the datetime object to the desired string format
    str_date = datetime_obj.strftime('%A %d %B %Y')

    # Return the converted string
    return str_date


# In this code, the `get_str_date` function takes a date string in ISO format as the input. It uses the `strptime` method from the `datetime` module to convert the input string into a datetime object. Then, it uses the `strftime` method to format the datetime object into the desired string format, which includes the day of the week, number, month, and year. Finally, the function returns the converted string.
# You can call the function like this:

date = '2021-05-27 17:08:34.149Z'
converted_date = get_str_date(date)
print(converted_date)  # Output: Thursday 27 May 2021

#To test the function, I used the example you gave me. Here is the result:

# Test the function with the example
print(get_str_date("2021-05-27 17:08:34.149Z")) # Output: Thursday 27 May 2021