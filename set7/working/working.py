# Accepted 12-hour format:
# + 9:00 AM to 5:00 PM
# + 9 AM to 5 PM
# AM and PM are case-sensitive and 
# there is no period and there is a space between them and the hour
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()