import re
from datetime import date
from vehicle import Vehicle, Car, Motorbike
import sys
import random as rd


def main():
    print("If you don'd know the info, please enter and skip the prompt!")
    print("** indicates that the field is required!")
    name = input("**Name: ")
    while True:
        try:
            qualified, age = check_age(input("**DOB: "))
            if qualified:
                sys.exit("You are not old enough to buy a vehicle!")
            else:
                break
        except TypeError:
            print("Invalid DOB! Please try again!")
            continue
    while True:
        if (city := input("**Your city: ").strip().title()) not in Vehicle.cities:
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


def plate_gen_or_check(index, vehicle, plate="29AA-51935"):
    # Format XXY-ZZZZZ where XX is a number from 11 to 99, Y is a letter (or AA/AB)
    if index == "0":  # Randomize the plate number
        nums = str(rd.randint(0, 99999))
        plate_nums = '0' * (5 - len(nums)) + nums
        if (type(vehicle) is Motorbike) and (not vehicle.type_of_motorbike()):
            seri = rd.choice("AA", "AB")
        else:
            seri = rd.choice(Vehicle.seri)
        city_num = rd.choice(Vehicle.cities[vehicle.city])
        return f"{city_num}{seri}-{plate_nums}" 
    if index == "1":  # Check the wanted plate
        if regis_plate := re.search(r"(^[1-9][1-9])([a-z][ab]?)-[0-9]{5}$", plate.strip(), flags=re.IGNORECASE):
            if regis_plate.group(1) not in Vehicle.cities[vehicle.city]:  # Valid number corresponding to the city
                raise ValueError("Not a valid city!")
            if regis_plate.group(2).upper() in ["AA", "AB"] and type(vehicle) is Motorbike and float(vehicle.type_of_motorbike()) > 50:
                raise ValueError("Not a valid seri!")
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