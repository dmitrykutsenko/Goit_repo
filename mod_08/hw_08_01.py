# Develop a Python function get_days_from_today(date) that will return the number of days from the current date, where the date parameter is a string of the format '2020-10-09' (year-month-day).
#
#Hints:
#1) The date parameter can be split into year, month and day using the split string method.
#2) datetime accepts arguments of type int, use type conversion.
#3) ignore hours, minutes and seconds for your date, full days are important.
#4) you can get the number of days by subtracting it from the current date specified in the date variable (without time).
#
#For example: If the current date is 'May 5, 2021', then the call to get_days_from_today("2021-10-09") should return -157
#
#So, a Python function that will return the number of days from the current date, where the date parameter is a string of the format '2020-10-09' (year-month-day).

# Import the datetime module
from datetime import datetime

# Define a function to get the number of days from the current date
def get_days_from_today(date):
    # Split the date parameter into year, month and day using the split string method
    #year, month, day = date.split('-')
    #print(year)
    #print(day)
    #print(month)
    # Convert the year, month and day to integers using type conversion
    #year = int(year)
    #month = int(month)
    #day = int(day)
    # Create a datetime object from the year, month and day
    #date = datetime.date(year, month, day)
    # Get the current date without time using the today method
    #today = datetime.date.today()
    # Subtract the date from the current date and get the number of days using the days attribute
    #days = (today - date).days
    # Return the number of days
    #return days
    #print(days)

    current_date = datetime.now().date()
    year, month, day = map(int, date.split('-'))
    given_date = datetime(year, month, day).date()
    days_difference = (current_date - given_date).days
    return days_difference

get_days_from_today("2021-10-09")