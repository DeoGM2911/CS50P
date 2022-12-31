# List of month
month_converter = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def check_for_date(date: str) -> bool:
    """Check for proper format of the input string

    Args:
        date: a string that represents a date in the USA format

    Returns: False if the date has an appropriate format and True if it doesn't
    """
    # Format MM/DD/YYY
    if '/' in date:
        if date.count('/') != 2:
            return True
        try:
            if not 1 <= int(date.split('/')[0]) <= 12:
                return True
            if not 1 <= int(date.split('/')[1]) <= 31:
                return True
        except ValueError:
            return True
        except IndexError:
            return True
    # Format Month DD, YYYY
    else:
        if date.count(',') != 1:
            return True
        if date.count(' ') != 2:
            return True
        try:
            if not 1 <= int(date.split(' ')[1].removesuffix(',')) <= 31:
                return True
            if date.split(' ')[0].title() not in month_converter:
                return True
        except ValueError:
            return True
        except IndexError:
            return True
    return False


while True:
    USA_format = input("US' date: ")
    # Check for correct format
    # Debug by splitting the if statement and reformat the while block
    if check_for_date(USA_format):
        continue
    # Take out the elements in the USA's format
    else:
        if '/' in USA_format:
            date_elements = USA_format.split('/')
            break
        elif ',' in USA_format:
            date_elements = USA_format.split(' ')
            break
# Convert the USA's format to the Universal format
# Reformat the year
year = date_elements[2]
if len(year) < 4:
    year = '0' * (4 - len(year)) + year
# Reformat the day and the month
# Function for reformatting day and month


def reformat(d_or_m: str):
    """Reformat the day or the month
        Arg: d_or_m (a string represents a date or a month)
        Returns: the reformatted version of the day or month (E.g. 1 -> 01)
    """
    if len(d_or_m) == 1:
        return '0' + d_or_m
    else:
        return d_or_m


# for the month DD, YYYY format
if date_elements[0] in month_converter:
    month = reformat(str(month_converter.index(date_elements[0]) + 1))
    day = reformat(date_elements[1].removesuffix(','))
# for the MM/DD/YYYY format
else:
    month = reformat(date_elements[0])
    day = reformat(date_elements[1])
# Generating the universal format YYYY-MM-DD
uni_format = f'{year}-{month}-{day}'
print(f"The date is: {uni_format}")
