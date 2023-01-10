# This program attempt to solve the problem "Vanity Plate" by using regular expression
# The biggest different between using regex and normal conditions is that regex can provide the correct patterns,
# while the conditions approach check all the wrong conditions
import re


def main():
    while True:
        plate = input("Plate: ")
        if len(plate) < 1: break
        if is_valid(plate):
            print("Valid")
        else:
            print("Invalid")


# The requirement of the number of characters between 2 and 6 is statisfied by the regex
# The requirement that the first two characters are letters is statisfied by the regex
# The re.IGNORECASE covers the issue of case-insensitivity
# The regex of valid plates are:
# * ^[a-z]{2}(?:[1-9][0-9]{3})?$
# * ^[a-z]{2,5}[1-9]$
# * ^[a-z]{2,4}[1-9][0-9]$
# * ^[a-z]{2,3}[1-9][0-9]{2}$
# We can use re.fullmatch() to eliminate ^ and $


def is_valid(plate: str) -> bool:
    if re.fullmatch(r"[a-z]{2}(?:[1-9][0-9]{3})?", plate, flags=re.IGNORECASE):
        return True
    elif re.fullmatch(r"[a-z]{2,5}[1-9]", plate, flags=re.IGNORECASE):
        return True
    elif re.fullmatch(r"[a-z]{2,4}[1-9][0-9]", plate, flags=re.IGNORECASE):
        return True
    elif re.fullmatch(r"[a-z]{2,3}[1-9][0-9]{2}", plate, flags=re.IGNORECASE):
        return True
    else: 
        return False


if __name__ == "__main__":
    main()