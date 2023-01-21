import re
from datetime import date
import sys
import random as rd
import time


class Vehicle:
    # list of provinces and cities in Vietnam
    cities = {
        "An Giang": ['67'], "Ba Ria-Vung Tau": ['72'], "Bac Lieu": ['94'], "Bac Giang": ['98'], "Bac Kan": ['97'],
        "Bac Ninh": ['99'], "Ben Tre": ['71'], "Binh Duong": ['61'], "Binh Dinh": ['77'], "Binh Phuoc": ['93'], 
        "Binh Thuan": ['86'], "Ca Mau": ['69'],"Cao Bang": ['11'], "Can Tho": ['65'], "Da Nang": ['43'], "Dak Lak": ['47'], 
        "Dak Nong": ['48'], "Dien Bien": ['27'], "Dong Nai": ['39', '60'], "Dong Thap": ['66'], "Gia Lai": ['81'], "Ha Giang": ['23'],
        "Hanoi": ['29', '30', '31', '32', '33', '40'], "Ha Tinh": ['38'],"Hai Duong": ['34'], "Hai Phong": ['15', '16'],
        "Hoa Binh": ['28'], "Hung Yen": ['89'], "Khanh Hoa": ['79'], "Kien Giang": ['68'], "Kon Tum": ['82'], "Lai Chau": ['25'],
        "Lang Son": ['12'], "Lao Cai": ['24'], "Lam Dong": ['49'], "Long An": ['62'], "Nam Dinh": ['18'], "Nghe An": ['37'],
        "Ninh Binh": ['35'], "Ninh Thuan": ['85'], "Phu Tho": ['19'], "Phu Yen": ['78'], "Quang Binh": ['73'], "Quang Nam": ['92'], 
        "Quang Ngai": ['76'], "Quang Ninh": ['14'], "Quang Tri": ['74'], "Soc Trang": ['83'], "Son La": ['26'], "Tay Ninh": ['70'], 
        "Thai Binh": ['17'], "Thai Nguyen": ['20'], "Thanh Hoa": ['36'], "Ha Nam": ['90'], "Hau Giang": ['95'],
        "Ho Chi Minh City": ['41', '50', '51', '52' ,'53', '54', '55', '56', '57', '58', '59'], "Thua Thien Hue": ['75'],
        "Tien Giang": ['63'], "Tra Vinh": ['84'], "Tuyen Quang": ['22'], "Vinh Long": ['64'], "Vinh Phuc": ['88'], "Yen Bai": ['21']
    }
    
    seri = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L', 'M', 'N', 'P', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    
    def __init__(self, cyl_capacity: float, price: float, city: str="Hanoi") -> None:
        self.cyl_capacity = cyl_capacity  # the vehicle's engine's capacity in cm^3
        self.price = price  # tax-not-included price in USD
        self.city = city
    
    def __str__(self):
        return f"""
* Note: if the value is None, it means that you haven't provided the info.
*** The vehicle's attributes are:
    - Power: {self.power} (HP)
    - Price: ${self.price}""".strip()
    
    @property
    def cyl_capacity(self):
        return self._cyl_capacity
    
    @cyl_capacity.setter
    def cyl_capacity(self, cyl_capacity):
        if float(cyl_capacity) < 0:
            raise ValueError("Not a valid number!")
        self._cyl_capacity = cyl_capacity
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if float(price) < 0:
            raise ValueError("Not a valid number!")
        self._price = price
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        if city not in Vehicle.cities.keys():
            raise ValueError("City not found!")
        self._city = city


class Car(Vehicle):
    tax_plate_regitration = {"Hanoi": 853.33, "Ho Chi Minh City": 469.33}  # other cities/provinces correspond to $42.67
    tax_regitration_fee = {"Hanoi": 0.12, "Danang": 0.12, "Haiphong": 0.12, "Ho Chi Minh City": 0.1, "Cantho": 0.1}
    # the VAT tax is 10% for all products
    
    def __init__(self, cyl_capacity: float, price: float, city: str="Hanoi"):
        super().__init__(cyl_capacity, price, city)
    
    def __str__(self):
        return super().__str__()


class Motorbike(Vehicle):
    def __init__(self, cyl_capacity: float, price: float, city: str="Hanoi") -> None:
        super().__init__(cyl_capacity, price, city)
    
    def __str__(self):
        return super().__str__()
    
    def type_motor(self):
        return self.cyl_capacity > 50
    


def main():
    print("Welcome!")
    print("This is the Vehicle program in which you can know the price and check/generate the license plate!")
    print("Enter esc in any question to escape the program!")
    print("Please note that (**) indicates that the field is required!")
    
	# Get the user's name
    name = input("(**) Name: ")
    if name == "esc":
        sys.exit("Successfully exit the program.")
    
    # Check the age condition of the user
    while True:
        try:
            print("The format for the DOB is DD/MM/YYYY or DD-MM-YYYY")
            dob = input("(**) DOB: ")
            if dob == "esc":
                sys.exit("Successfully exit the program.")
            if check_age(dob=dob):
                sys.exit("You are not old enough to buy a vehicle!")
            else:
                break
        except ValueError:
            print("Invalid DOB! Please try again!")
    
    # Get the user's city where he/she buys the vehicle
    while True:
        if (city := input("(**) Your city: ").strip().title()) not in Vehicle.cities:
            print("Invalid city! Please try again!")
            continue
        if city == "Esc":
            sys.exit("Successfully exit the program.")
        else:
            break
    
    # Get the attributes of the vehicle
    while True:
        print('Please enter "car" or "motorbike" and it is case-insensitive.')
        _vehicle = input("(**) Vehicle's type: ").lower()
        if _vehicle == "esc":
                sys.exit("Successfully exit the program.")
    
        if _vehicle == "car" or _vehicle == "motorbike":
            break
        else:
            print("Invalid type of vehicle! Please enter car or motorbike!")
    
    while True:
        try:
            cyl_vol = input("(**) Vehicle's cylinder volume (in cm^3): ").lower()
            if cyl_vol == "esc":
                sys.exit("Successfully exit the program.")
            
            price = input("(**) The vehicle's price (tax not included) (in USD): ").lower()
            if price == "esc":
                sys.exit("Successfully exit the program.")
        except ValueError:
            continue
        
        if _vehicle == "car":
            try:
                vehicle = Car(float(cyl_vol), float(price), city)
                break
            except ValueError:
                print("Please check your vehicle's attributes!")
                continue
        elif _vehicle == "motorbike":
            try:
                vehicle = Motorbike(float(cyl_vol), float(price), city)
                break
            except ValueError:
                print("Please check your vehicle's attributes!")
                continue
    
    # Prompt the user for the feature they wish to use
    while True:
        feat = input("""***********************************************************
* Please input the following numbers corresponding to the features you want to use:
0: Generate a random license plate.
1: Check your desired license plate. Input in the form of 1 LICENSEPLATE.(Sample Input: 1 29M-02453) 
(Be aware of white spaces between the number 1 and the license plate)
2: Check the total value for registrating the vehicle.
3: Check your vehicle's details.
4: Exit the program.
***********************************************************\nNumber: """).strip()
        
        if feat == "4":
            sys.exit("Thank you for using the product!")
        
        elif feat == '0':
            print("PLease wait! Generating license plate.....")
            time.sleep(1)
            print("Your license plate is: ", plate_gen_or_check(feat, vehicle))
        
        elif feat.split(" ")[0] == '1':
            try:
                if plate_gen_or_check('1', vehicle, feat.split(" ")[1]):
                    print("____This is a valid plate!____")
                else:
                    print("____This is an invalid plate!____")
            except IndexError:
                print("Please also enter the desired license plate!")
            except ValueError:
                print("Not a valid plate! Please check your city number and seri!")
        
        elif feat == "2":
            print(regis_fee(vehicle))
            print("The components are:")
        
        elif feat == "3":
            print(f"User: {name}\nDate of birth: {dob}\nType of vehicle: {_vehicle.capitalize()}\n{vehicle}")
        
        else:
            print("Please enter a number!")


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
        if regis_plate := re.search(r"(^[1-9][0-9])([a-z][ab]?)-[0-9]{5}$", plate.strip(), flags=re.IGNORECASE):
            if regis_plate.group(1) == "10":
                raise ValueError("Not a valid starting number!")
            if regis_plate.group(1) not in Vehicle.cities[vehicle.city]:  # Valid number corresponding to the city
                raise ValueError("Not a valid city!")
            # Only motorbike with the engine's volume less than 50 would have the seri of AA or AB
            # Check for motorbike
            if type(vehicle) is Motorbike:
                if regis_plate.group(2).upper() in ["AA", "AB"] and vehicle.type_motor():
                    raise ValueError("Not a valid seri!")
                if regis_plate.group(2).upper() not in ["AA", "AB"] and (not vehicle.type_motor()):
                    raise ValueError("Not a valid seri!")
                else:
                    return True
            # Check for car
            else:
                if regis_plate.group(2).upper() in ["AA", "AB"] and type(vehicle) is Car:
                    raise ValueError("Not a valid seri!")
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
        bool: False if the user age is qualified
    """
    today = date.today()
    if find_day := re.search(r"(^(?:[0-3])?[0-9])(?:-|/)((?:[0-1])?[0-9])(?:/|-)([0-9]{4}$)", dob.strip()):
        try:
            if (day := date(int(find_day.group(3)), int(find_day.group(2)), int(find_day.group(1)))) > today:
                raise ValueError("Not a valid DOB!")
        except ValueError:
            raise ValueError("Not a valid DOB!")
    else: 
        raise ValueError("Not a valid DOB!")
    
    return (today - day).days <= 18 * 365  # Less than 18 year old


def regis_fee(vehicle):
    """Get the total price include tax of the vehicle
    
    Args:
        vehicle (Car|Motorbike): the type of vehicle (car or motorbike) 

    Returns:
        str: the formated string that show the total price of the vehicle
    """
    if type(vehicle) is Car:
        if vehicle.city not in Car.tax_regitration_fee.keys():
            return f"Total: ${float(vehicle.price) * 1.1 + 42.67:.2f}"
        elif vehicle.city in Car.tax_regitration_fee.keys() and vehicle.city not in Car.tax_plate_regitration.keys():
            return f"Total: ${float(vehicle.price) * (1.1 + Car.tax_regitration_fee[vehicle.city]) + 42.67:.2f}"
        elif vehicle.city == "Hanoi" or vehicle.city == "Ho Chi Minh City":
            return f"Total: ${float(vehicle.price) * (1.1 + Car.tax_regitration_fee[vehicle.city]) + Car.tax_plate_regitration[vehicle.city]:.2f}"
    if type(vehicle) is Motorbike:
        if float(vehicle.price) < 639.66:
            return f"Total: ${float(vehicle.price) * 1.1 + 31.98:.2f}"
        elif 1705.76 >= float(vehicle.price) >= 639.66:
            return f"Total: ${float(vehicle.price) * 1.1 + 63.97:.2f}"
        else:
            return f"Total: ${float(vehicle.price) * 1.1 + 127.93:.2f}"



if __name__ == "__main__":
    main()
