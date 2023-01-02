# This is for the 24-hour interval


def main():
    time = input("What time is it? \n")
    # format: NN:NN where N can be any number from 0 to 9
    if (convert24(time) - 7 >= 0) and (convert24(time) - 8 <= 0):
        print("breakfast")
    elif (convert24(time) - 12 >= 0) and (convert24(time) - 13 <= 0):
        print("lunch")
    elif (convert24(time) - 18 >= 0) and (convert24(time) - 19 <= 0):
        print("dinner")


def convert24(time):
    minute = int(time.split(':')[1]) / 60
    hour = float(time.split(':')[0])
    return hour + minute


if __name__ == "__main__":
    main()

# This is for the 12-hour interval

"""
def main1():
    time = convert12(input("What time is it? \n"))
    #format: NN:NN a.m. or NN:NN p.m. ; N is any number from 0 to 9
    try:
        if (convert12(time) - 7 >= 0) and (convert12(time) - 8 <= 0):
            print("breakfast")
        elif (convert12(time) - 12 >= 0) and (convert12(time) - 13 <= 0):
            print("lunch")
        elif (convert12(time) - 18 >= 0) and (convert12(time) - 19 <= 0):
            print("dinner")
    except ValueError:
        print("Invalid format!")


# We could move the conditionals in the main1() function down instead
# The convert12 function will then return the meal time


def convert12(time):
    '''Convert time to a floating point
    Args:
        time (_type_): in form of NN:NN a.m. or NN:NN p.m.
    Returns:
        a floating point tha represent the hour has passed by since 12:00 p.m.
    '''
    hour_and_min = time.split(' ')[0].split(':')
    minute = int(hour_and_min[1])/60
    hour = float(hour_and_min[0])
    if time_elements[1] == "p.m.":
        hour = hour + 12
    time_converted = hour + minute
    return time_converted


if __name__ == "__main__":
    main1()
    """
