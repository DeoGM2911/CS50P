# This program attempt to solve the problem "Vanity Plate" by using regular expression
import re

plate = input("Plate: ")

# The requirement of the number of characters between 2 and 6 is statisfied
# The requirement that the first two characters are letters
# The re.IGNORECASE covers the issue of case-insensitivity
def is_valid(plate: str) -> bool:
    if plate_el := re.match(r"[a-z]{2}([a-z0-9]{0,4}$)", plate, flags=re.IGNORECASE):
        if len(plate_el.group(1)) < 1:  # If no additional character
            return True
        else:
            pass
    
    else:
        return False