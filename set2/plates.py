def main():
    while True:
        plate = input("Plate: ").upper()
        if plate == "": break
        if is_valid(plate):
            print("Valid")
        else:
            print("Invalid")


def is_valid(s: str):
    special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'
                    '{', '}', '[', ']', ':', ';', '"', "'", ',', '<',
                    '.', '>', '?', '?', '|', '`', '~', '-', '_', '+',
                    '=', "\\"]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # requirement No.1: 2<= length <=6
    if not 2 <= len(s) <= 6:
        return False
    # requirement No.4: no special character
    for i in range(2 - len(s), 0):
        if s[i] in special_char:
            return False

    # requirement No.2: start with 2 letters
    for letter in s[:2]:
        if letter in numbers:
            return False
    if len(s) == 2:  # If the length of the plate is only 2, then it is valid
        return True
    
    # Check the last number of requirement 3
    if not s[-1] in numbers:
        return False
    if len(s) == 3 and s[-1] != "0": # If the length of the plate is 3, then it is valid
        return True

    # requirement No.3: letter can't be the end of the plate and number can't be in the middle
    # for all other characters. The first two chars 've already satisfied the conditions.
    # for length of 4, 5, 6
    if not s[-2] in numbers:  # The case when the char right before the end is a letter
        if s[-1] == '0':
            return False
        elif len(s) == 5 and s[-3] in numbers:
            return False
        elif len(s) == 6:
            if s[-3] in numbers:
                return False
            else:
                if s[-4] in numbers:
                    return False
    else:  # The case when the char right before the end is a number
        if s[-2] == 0 and len(s) == 4:
            return False  # if the length of the string is 4
        elif len(s) == 5:  # if the length of the string is 5
            if s[-3] == '0':
                return False
            elif (not s[-3] in numbers) and (s[-2] == '0'):
                return False
        elif len(s) == 6:  # if the length of the string is 6
            if (not s[-3] in numbers) and (not s[-4] in numbers) and (s[-2] == '0'):
                return False
            elif (s[-3] == '0') and (not s[-4] in numbers):
                return False
            elif (s[-4] in numbers) and (not s[-3] in numbers):
                return False
            elif (s[-3] in numbers) and s[-4] == '0':
                return False
    return True


if __name__ == "__main__":
    main()
