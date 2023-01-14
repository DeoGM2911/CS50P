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
    
    
    def reformat(hr: str) -> str:    
        if ":" not in hr:
            if len(hr) == 1:
                hr = f"0{hr}:00"
            else:
                hr = f"{hr}:00"
        else:
            if len(hr.split(':')[0]) == 1:
                hr = f"0{hr.split(':')[0]}:{hr.split(':')[1]}"
            else:
                hr = f"{hr.split(':')[0]}:{hr.split(':')[1]}"
        return hr
    
    
    # Reformat the user's input (E.g 9 AM -> 09:00).
    start = reformat(start)
    end = reformat(end)
    
    # Convert 12:xx AM to 00:xx. This part go after the reformat because this block assume the format has a semi-colon.
    if (hour.group(1).split(" ")[0].split(":")[0] == "12") and (hour.group(1).split(" ")[1] == "AM"):
        start = f"00:{start.split(':')[1]}"
    if (hour.group(2).split(" ")[0].split(":")[0] == "12") and (hour.group(2).split(" ")[1] == "AM"):
        end = f"00:{end.split(':')[1]}"

    return f"{start} to {end}"


if __name__ == "__main__":
    main()
