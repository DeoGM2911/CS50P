import re
from datetime import date
from vehicle import Vehicle, Car, Motorbike
import sys


def main():
    print("If you don'd know the info, please enter and skip the prompt!")
    print("** indicates that the field is required!")
    name = input("**Name: ")
    while True:
        date_of_birth = input("**DOB: ")
        try:
            if check_age(date_of_birth)[0]:
                sys.exit("You are not old enough to buy a vehicle!")
            else:
                break
        except TypeError:
            print("Invalid DOB! Please try again!")
            continue
    while True:
        if (city := input("**Your city: ")) not in Vehicle.cities:
            print("Invalid city! Please try again!")
            continue
        else:
            break
    _vehicle = input("**Vehicle's type: ")
    while True:
        if _vehicle == "car" or _vehicle == "motorbike":
            break
        else:
            print("Invalid type of vehicle! Please enter car or motorbike!")
            continue
    while True:
        try:
            cyl_vol = input("**Vehicle's cylinder volume (in cm^3): ")
            price = input("**The vehicle's price (tax not included) (in USD): ")
            if len(power := input("The vehicle's power (in HP): ").strip()) < 1:
                power = None
            if len(max_tor := input("The vehicle's max torsion: ").strip()) < 1:
                max_tor = None
            if len(mass := input("The vehicle's mass (in tons): ").strip()) < 1:
                mass = None
            if _vehicle == "car":
                while True:
                    try:
                        if len(passenger_capa := input("The car's capacity: ").strip()) < 1:
                            passenger_capa = None
                        if len(max_load := input("The car's max load (in tons): ")) < 1:
                            max_load = None
                        vehicle = Car(cyl_vol, price, max_tor, mass, power, max_load, passenger_capa, city)
                        break
                    except ValueError:
                        continue
            elif _vehicle == "motorbike":
                vehicle = Motorbike(cyl_vol, price, max_tor, mass, power, city)
        except ValueError:
            print("Please check your vehicle's attributes!")
            continue
    ########## Create an input for addtional support with methods for car and motorbike


def plate_gen_or_check(plate):
    pass


def check_age(dob):
    """_summary_

    Args:
        dob (str): the date of birth. Accepted format: DD/MM/YYYY or DD-MM-YYYY
    
    Returns:
        bool: True if the user age is qualified
    """
    today = date.today()
    if find_day := re.match(r"(^(?:[0-3])?[0-9])(?:-|/)(?:[0-1])?[0-9])(?:/-)([0-9]{4})", dob.strip()):
        try:
            if (day := date(int(find_day.group(1)), int(find_day.group(2)), int(find_day.group(3)))) > today:
                raise TypeError("Not a valid DOB!")
        except ValueError:
            raise TypeError("Not a valid DOB!")
    else: 
        raise TypeError("Not a valid DOB!")
    
    return (today - day).days <= 18 * 365, (today - day).days  # Less than 18 year old


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