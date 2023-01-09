from datetime import date
import sys
import re
import inflect
p = inflect.engine()
# Prompt the user for his/her DOB in form of YYYY-MM-DD
# Calculate the age of the user in minutes, rounded to the nearest integer
# By default, the today's date and the DOB is set to be 00:00:00 by the date object
# In this program I accept day (and month) in either form: 02 or 2



def main():
    date_of_birth = input("What's your birthday? \n")
    checker, dob = get_dob(date_of_birth, date.today())
    if not checker:
        sys.exit("Invalid date of birth! Please retry!")
    else:
        print(f"{sing(-(dob - date.today()).days * 24 * 60)} minutes")


def get_dob(day: str, today: date) -> bool:
    """Check whether a day is a valid date of birth
    Args:
        day (str): the inputed date of birth
        today (date): today's date
    Returns:
        bool: False if invalid date, True if valid. The following "None" after each False == a placeholder for _day
        _day (date): the valid date of birth
    """
    if find_day := re.match(r"(^[0-9]{4})-((?:[0-1])?[0-9])-((?:[0-3])?[0-9]$)", day):
        try:
            if (_day := date(int(find_day.group(1)), int(find_day.group(2)), int(find_day.group(3)))) > today:
                return False, None
        except ValueError:
            return False, None
    
    else: 
        return False, None
    
    return True, _day


def sing(minutes: int) -> str:
    """ Turn an integer to its English word form
    Args:
        minutes (int): an integer
    Returns:
        str: the English form of that integer
    """
    return p.number_to_words(minutes , andword="").capitalize()


if __name__ == "__main__":
    main()
