def main():
    print(validate_no_regex(input("Enter: ")))


def validate_no_regex(ip: str) -> bool:
    """
        This function have the exact same function as the one which uses regex.
        However, this function don't use regex.
    Args:
        ip (str): an IPv4 Address if passed all test
                else it isn't
    Returns: bool
        True means proper IPv4 Address
        False means inproper address
    """
    # Check whether there are 4 componets and 3 dots.
    if ip.count(".") != 3:
        return False
    comps = ip.split('.')
    # Check if the components of the IP Address are numbers.
    try:
        list_of_comp = list(map(int, comps))
    except ValueError:
        return False
    # Check if there is any whitespace or escape sequence.
    # This block is only needed if the user inputs anything  different form numbers and dots.
    for string, integer in zip(comps, list_of_comp):
        if len(string) != len(str(integer)):
            return False
    # Check if the numbers are in the range [0,255].
    for num in list_of_comp:
        if (0 > num) or (num > 255):
            return False
    return True


if __name__ == "__main__":
    main()