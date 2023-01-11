# Accepted 12-hour format:
# + 9:00 AM to 5:00 PM
# + 9 AM to 5 PM
# AM and PM are case-sensitive and
# there is no period and there is a space between them and the hour.
import re


def main():
    print(convert(input("Hours: ")))


def convert(inp: str):
    hour = re.search(r"(^[0-9]+(?::[0-5][0-9])? (?:AM|PM)) to ([0-9]+(?::[0-5][0-9])? (?:AM|PM)$)", inp.strip())
    if hour is None:
        raise ValueError

    # Take out the starting hour and the ending hour.
    for hr in [hour.group(1), hour.group(2)]:
        # Check for valid hour
        if (int(hr.split(" ")[0].split(":")[0]) > 12) or (int(hr.split(" ")[0].split(":")[0]) <= 0):
            raise ValueError

    start = re.sub(r" (?:AM|PM)", "", hour.group(1))
    end = re.sub(r" (?:AM|PM)", "", hour.group(2))

    # If the hour is in the PM, we add 12 to its hour part of the starting and/or ending hour.
    if hour.group(1).split(" ")[1] == "PM" and (hour.group(1).split(" ")[0].split(":")[0] != "12"):
        start = re.sub(r"[0-9]+", str(int(start.split(":")[0]) + 12), start, count=1)
    if hour.group(2).split(" ")[1] == "PM" and (hour.group(2).split(" ")[0].split(":")[0] != "12"):
        end = re.sub(r"[0-9]+", str(int(end.split(":")[0]) + 12), end, count=1)

    # Reformat if the user's input doesn't have the minute part (E.g 9 AM -> 09:00).
    if ":" not in start:
        if len(start) == 1:
            start = f"0{start}:00"
        else:
            start = f"{start}:00"
    if ":" not in end:
        if len(end) == 1:
            end = f"0{end}:00"
        else:
            end = f"{end}:00"

    # Convert 12:xx AM to 00:xx.
    if (hour.group(1).split(" ")[0].split(":")[0] == "12") and (hour.group(1).split(" ")[1] == "AM"):
        start = f"00:{start.split(':')[1]}"
    if (hour.group(2).split(" ")[0].split(":")[0] == "12") and (hour.group(2).split(" ")[1] == "AM"):
        end = f"00:{end.split(':')[1]}"

    return f"{start} to {end}"


if __name__ == "__main__":
    main()
#####################################################################################################