import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    """
    This function use regex and show whether a string is a valid IPv4 Address.
    Args:
        ip (str): an IPv4 Address if passed all test, else it isn't
                HAS TO BE IN THE FORMAT "XXX.XXX.XXX.XXX", where XXX is an integer in th range [0,255]

    Returns: bool:
        True means proper IPv4 Address
        False means inproper address
    """
    # EXPECT a format of A.B.C.D with A, B, C, and D are integers in the [0, 255] range.
    ipv4 = re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ip)
    if ipv4 is None:
        return False
    nums = ipv4.group(0).split(".")
    for num in nums:
        if int(num) > 255 or int(num) < 0:
            return False
    return True


if __name__ == "__main__":
    main()