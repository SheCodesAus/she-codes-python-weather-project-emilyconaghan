import csv
from datetime import datetime
from datetime import date

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


# print(format_temperature("32"))

# pass all tests into run tests. If you do run it and call the function - it will be debugging

print("new code")


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    date_list = list(iso_string[0:10])

    year = date_list[0:4]
    month = date_list[5:7]
    day = date_list[8:]

    str_year = ""
    str_month = ""
    str_day = ""
    output_month = ""

    for a in year:
        str_year += a

    for b in month:
        str_month += b

    for c in day:
        str_day += c

    output_iso_day = date(int(str_year), int(
        str_month), int(str_day)).isoweekday()  # interger assigned to day of the week - Mo = 1, Tu=2, We=3, Th=4, Fr=5, Sa=6, Su=7
    # output day variables
    if output_iso_day == 1:
        output_day = 'Monday'
    if output_iso_day == 2:
        output_day = 'Tuesday'
    if output_iso_day == 3:
        output_day = 'Wednesday'
    if output_iso_day == 4:
        output_day = 'Thursday'
    if output_iso_day == 5:
        output_day = 'Friday'
    if output_iso_day == 6:
        output_day = 'Saturday'
    if output_iso_day == 7:
        output_day = 'Sunday'

       # output month variables

    if int(str_month) == 1:
        output_month = 'January'
    if int(str_month) == 2:
        output_month = 'February'
    if int(str_month) == 3:
        output_month = 'March'
    if int(str_month) == 4:
        output_month = 'April'
    if int(str_month) == 5:
        output_month = 'May'
    if int(str_month) == 6:
        output_month = 'June'
    if int(str_month) == 7:
        output_month = 'July'
    if int(str_month) == 8:
        output_month = 'August'
    if int(str_month) == 9:
        output_month = 'September'
    if int(str_month) == 10:
        output_month = 'October'
    if int(str_month) == 11:
        output_month = 'November'
    if int(str_month) == 12:
        output_month = 'December'

    return f"{output_day} {(str_day)} {output_month} {str_year}"


# print(convert_date("2021-07-05T07:00:00+08:00"))


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_celcius = (float(temp_in_farenheit) - 32) * (5/9)
    return round(temp_in_celcius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    num_list = []

    for items in weather_data:
        num_list.append(float(items))
    weather_data = num_list

    return sum(weather_data) / len(weather_data)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    output = []
    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            print(line)
            output.append(line)
    return output


print(load_data_from_csv("tests/data/example_one.csv"))


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    min_list = []

    for items in weather_data:
        min_list.append(float(items))
    weather_data = min_list

    min_value = weather_data[0]
    min_location = 0
    index = 0

    for num in weather_data:
        if num < min_value:
            min_value = num
            min_location = index
        if num == min_value:
            min_value = num
            min_location = index
        index += 1

    output_values = (float(min_value), float(min_location))
    return output_values


# print(find_min([]))


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """

    max_list = []

    for items in weather_data:
        max_list.append(float(items))
    weather_data = max_list

    max_value = weather_data[0]
    max_location = 0
    index = 0

    for num in weather_data:
        if num > max_value:
            max_value = num
            max_location = index
        if num == max_value:
            max_value = num
            max_location = index
        index += 1

    output_values = (float(max_value), float(max_location))
    return output_values


# print(find_max([]))


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
