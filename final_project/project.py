import re
from datetime import date
from vehicle import Vehicle, Car, Motorbike
import sys
import random as rd
import time


def main():
    print("If you don'd know the info, please enter and skip the prompt!")
    print("Enter esc to escape the program!")
    print("** indicates that the field is required!")
    
	# Get the user's name
    name = input("**Name: ")
    if name == "esc":
        sys.exit("Successfully exit the program.")
    
    # Check the age condition of the user
    while True:
        try:
            qualified = check_age(input("**DOB: "))
            if qualified == "esc":
                sys.exit("Successfully exit the program.")
            if qualified:
                sys.exit("You are not old enough to buy a vehicle!")
            else:
                break
        except TypeError:
            print("Invalid DOB! Please try again!")
            continue
    
    # Get the user's city where he/she buys the vehicle
    while True:
        if (city := input("**Your city: ").strip().title()) not in Vehicle.cities:
            print("Invalid city! Please try again!")
            continue
        if city == "esc":
            sys.exit("Successfully exit the program.")
        else:
            break
    
    # Get the attributes of the vehicle
    while True:
        _vehicle = input("**Vehicle's type: ").lower()
        if _vehicle == "esc":
                sys.exit("Successfully exit the program.")
    
        if _vehicle == "car" or _vehicle == "motorbike":
            break
        else:
            print("Invalid type of vehicle! Please enter car or motorbike!")
            continue
    
    while True:
        cyl_vol = input("**Vehicle's cylinder volume (in cm^3): ")
        price = input("**The vehicle's price (tax not included) (in USD): ")
        if len(power := input("The vehicle's power (in HP): ").strip()) < 1:
            power = None
        if len(max_tor := input("The vehicle's max torsion: ").strip()) < 1:
            max_tor = None
        if len(mass := input("The vehicle's mass (in tons): ").strip()) < 1:
            mass = None
        if _vehicle == "car":
            if len(passenger_capa := input("The car's capacity: ").strip()) < 1:
                passenger_capa = None
            if len(max_load := input("The car's max load (in tons): ")) < 1:
                max_load = None
            try:
                vehicle = Car(cyl_vol, price, max_tor, mass, power, max_load, passenger_capa, city)
                break
            except ValueError:
                print("Please check your vehicle's attributes!")
                continue
        elif _vehicle == "motorbike":
            try:
                vehicle = Motorbike(cyl_vol, price, max_tor, mass, power, city)
                break
            except ValueError:
                print("Please check your vehicle's attributes!")
                continue
    
    # Prompt the user for the feature they wish to use
    while True:
        feat = input("""******************
        * Please input the following numbers corresponding to the features you want to use:
        0: Generate a random liscense plate.
        1: Check your desired liscense plate. Also type your liscense plate right next to the number 1.
        (PLease be aware of white spaces)
        2: Check the total value for registrating the vehicle.
        3: Check your vehicle's details.
        4: Exit the program.\nNumber: """).strip()
        
        if feat == "4":
            sys.exit("Thank you for using the product!")
        
        if feat == '0':
            print("Generating license plate.....")
            time.sleep(1)
            print(plate_gen_or_check(feat, vehicle))
            continue
        
        if feat.split(" ")[0] == '1':
            try:
                if plate_gen_or_check('1', vehicle, feat.split(" ")[1]):
                    print("Valid")
                else:
                    print("Invalid")
                    continue
            except IndexError:
                print("Please also enter the desired license plate!")
                continue
        
        if feat == "2":
            print(vehicle)
            continue
        
        if feat == "3":
            print(vehicle)
        
        else:
            print("Please enter a number!")
            continue


def plate_gen_or_check(index, vehicle, plate="29AA-51935"):
    """Return a license plate or check whether a license plate is valid

    Args:
        index (str): decide which mode the function would work (0 or 1)
        vehicle (Car or Motorbike): the class of the registered vehicle
        plate (str, optional): The plate number to check. Defaults to "29AA-51935".

    Raises:
        ValueError: if the plate isn't valid.
    Returns:
        str: the license plate num (mode 0)
        bool: for checking the plate (mode 1)
    """
    # Format XXY-ZZZZZ where XX is a number from 11 to 99, Y is a letter (or AA/AB)
    if index == "0":  # Randomize the plate number
        nums = str(rd.randint(0, 99999))
        plate_nums = '0' * (5 - len(nums)) + nums
        if (type(vehicle) is Motorbike) and (not vehicle.type_motor()):
            seri = rd.choice(["AA", "AB"])
        else:
            seri = rd.choice(Vehicle.seri)
        city_num = rd.choice(Vehicle.cities[vehicle.city])
        return f"{city_num}{seri}-{plate_nums}"
    
    if index == "1":  # Check the wanted plate
        if regis_plate := re.search(r"(^[1-9][1-9])([a-z][ab]?)-[0-9]{5}$", plate.strip(), flags=re.IGNORECASE):
            if regis_plate.group(1) not in Vehicle.cities[vehicle.city]:  # Valid number corresponding to the city
                raise ValueError("Not a valid city!")
            # Only motorbike with the engine's volume less than 50 would have the seri of AA or AB
            if type(vehicle) is Motorbike:
                if regis_plate.group(2).upper() in ["AA", "AB"] and vehicle.type_motor():
                    raise ValueError("Not a valid seri!")
                if regis_plate.group(2).upper() not in ["AA", "AB"] and (not vehicle.type_motor()):
                    raise ValueError("Not a valid seri!")
                else:
                    return True
            else:
                return True
        else:
            raise ValueError("Not a valid plate!")
    else:
        print("Please enter 0 or 1!")
        return False


def check_age(dob):
    """_summary_

    Args:
        dob (str): the date of birth. Accepted format: DD/MM/YYYY or DD-MM-YYYY
    
    Returns:
        bool: True if the user age is qualified
    """
    today = date.today()
    if find_day := re.search(r"(^(?:[0-3])?[0-9])(?:-|/)((?:[0-1])?[0-9])(?:/|-)([0-9]{4}$)", dob.strip()):
        try:
            if (day := date(int(find_day.group(3)), int(find_day.group(2)), int(find_day.group(1)))) > today:
                raise TypeError("Not a valid DOB!")
        except ValueError:
            raise TypeError("Not a valid DOB!")
    else: 
        raise TypeError("Not a valid DOB!")
    
    return (today - day).days <= 18 * 365  # Less than 18 year old


def regis_fee(vehicle, prc, city):
    """Get the total price include tax of the vehicle
    
    Args:
        vehicle (str): the type of vehicle (car or motorbike) 
        prc (float): the price of the vehicle (tax not included) 
        city (str): the name of the city where the vehicle is bought 

    Returns:
        str: the formated string that show the total price of the vehicle
    """
    if type(vehicle) is Car:
        return Car(0, 0, prc, city=city).get_tot_price_car()  # Only the price and city are needed so other params are 0
    if type(vehicle) is Motorbike:
        return Motorbike(0, 0, prc).get_tot_price_motorbike()  # Only the price is needed so other params are 0


if __name__ == "__main__":
    main()