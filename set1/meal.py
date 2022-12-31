#This is for the 24-hour interval
"""def main():
    time = input("What time is it? \n")
    #format: NN:NN where N can be any number from 0 to 9
    if convert(time)-7>=0 and convert(time)-8<=0:
        print("It's breakfast time.")
    elif convert(time)-12>=0 and convert(time)-13<=0:
        print("It's lunch time.")
    elif convert(time)-18>=0 and convert(time)-19<=0:
        print("It's dinner time.") 
def convert(time):
    time_elements = time.split(':')
    minute = int(time_elements[1])/60
    hour = float(time_elements[0])
    time_converted = hour + minute
    return time_converted
if __name__ == "__main__":
    main()"""

#This is for the 12-hour interval
def main1():
    time = input("What time is it? \n")
    #format: NN:NN a.m. or NN:NN p.m. ; N is any number from 0 to 9
    if convert1(time)-7>=0 and convert1(time)-8<=0:
        print("It's breakfast time.")
    elif convert1(time)-12>=0 and convert1(time)-13<=0:
        print("It's lunch time.")
    elif convert1(time)-18>=0 and convert1(time)-19<=0:
        print("It's dinner time.") 
def convert1(time):
    """Convert time to a floating point

    Args:
        time (_type_): in form of NN:NN a.m. or NN:NN p.m.

    Returns:
        a floating point tha represent the hour has passed by since 12:00 p.m.
    """
    time_elements = time.split(' ')
    hour_and_min = time_elements[0].split(':')
    minute = int(hour_and_min[1])/60
    hour = float(hour_and_min[0])
    if time_elements[1] == "p.m.":
        hour = hour + 12
    time_converted = hour + minute
    return time_converted
if __name__ == "__main__":
    main1()