import re
from datetime import date
import sys
import random as rd
from tabulate import tabulate
import keyboard


class Vehicle:
    # list of provinces and CITIES in Vietnam
    CITIES = {
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

    SERI = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L', 'M', 'N', 'P', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

    def __init__(self, cyl_capacity: float|int, price: float|int, city: str="Hanoi") -> None:
        self.cyl_capacity = cyl_capacity  # the vehicle's engine's capacity in cm^3
        self.price = price  # tax-not-included price in USD
        self.city = city

    def __str__(self) -> str:
        attrs = [["Engine's volume", f"{self.cyl_capacity:.2f} cm^3"], ["Price", f"${self.price:.2f}"]]
        return f"""
________________The vehicle's attributes_______________
{tabulate(attrs, headers=["Attribute", "Value"], tablefmt="grid", numalign="center")}""".strip()

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
        if city not in Vehicle.CITIES.keys():
            raise ValueError("City not found!")
        self._city = city


class Car(Vehicle):
    TAX_PLATE_REGIS = {"Hanoi": 853.33, "Ho Chi Minh City": 469.33}  # other cities/provinces correspond to $42.67
    TAX_REGIS_PER = {"Hanoi": 0.12, "Danang": 0.12, "Haiphong": 0.12, "Ho Chi Minh City": 0.1, "Cantho": 0.1}
    # the VAT tax is 10% for all products

class Motorbike(Vehicle):
    def checked(self):
        return self.cyl_capacity > 50


def main():
    print("_" * 22, "Welcome to Vplate", "_" * 22, sep="")
    print("This is the Vehicle program in which you can know the price and check/generate the license plate!")
    print("Enter esc in any question to escape the program!")
    print("Please note that (**) indicates that the field is required!")
    print("Press Space to continue!")
    print("_" * 51)
    keyboard.wait("space")

	# Get the user's name
    if (name := input("(**) Name:").strip()).lower() == "esc":
        sys.exit("Successfully exit the program.")

    # Check the age condition of the user
    while True:
        try:
            print("NOTE: The format for the DOB is DD/MM/YYYY or DD-MM-YYYY.")
            if (dob := input("(**) DOB: ")).lower() == "esc":
                sys.exit("Successfully exit the program.")
            if check_age(dob=dob):
                sys.exit("You are not old enough to buy a vehicle!")
            else:
                break
        except ValueError:
            print("Invalid DOB! Please try again!\n")

    # Get the user's city where he/she buys the vehicle
    while True:
        if (city := input("(**) Your city: ").strip().capitalize()) not in Vehicle.CITIES:
            print("Invalid city! Please try again!\n")
            continue
        if city == "Esc":
            sys.exit("Successfully exit the program.")
        else:
            break

    # Get the attributes of the vehicle
    while True:
        print('Please enter "car" or "motorbike" and it is case-insensitive.')
        if (_vehicle := input("(**) Vehicle's type: ").lower()) == "esc":
                sys.exit("Successfully exit the program.")

        if _vehicle == "car" or _vehicle == "motorbike":
            break
        else:
            print("Invalid type of vehicle! Please enter car or motorbike!\n")

    while True:
        try:
            if (cyl_vol := input("(**) Vehicle's engine volume (in cm^3): ").lower()) == "esc":
                sys.exit("Successfully exit the program.")
            if (cyl_volume := float(cyl_vol)) < 0:
                print("\n*Please check your vehicle's engine's volume!\n")
                continue
            break
        except ValueError:
            print("\n*Please check your vehicle's engine's volume!\n")

    while True:
        try:
            if (prc := input("(**) The vehicle's price (tax not included) (in USD): ").lower()) == "esc":
                sys.exit("Successfully exit the program.")
            if (price := float(prc)) < 0:
                print("\n*Please check your vehicle's price!\n")
                continue
            break
        except ValueError:
            print("\n*Please check your vehicle's price!\n")

    if _vehicle == "car":
        vehicle = Car(cyl_volume, price, city)
    elif _vehicle == "motorbike":
        vehicle = Motorbike(cyl_volume, price, city)

    # Prompt the user for the feature they wish to use
    while True:
        feat = input("""
***********************************************************
* Please input the following numbers corresponding to the features you want to use:
(0): Generate a random license plate.
(1): Check your desired license plate.(PLease only input 1 then Enter) 
(2): Check the total value for registrating the vehicle.
(3): Check the details.
(4): Exit the program.
***********************************************************
Number: """).strip()

        if feat == "4":
            sys.exit("\n" + "_" * 15 + "Thank you for using the product!" + "_" * 15)

        elif feat == '0':
            print("\nPLease wait! Generating license plate.....")
            print("Your license plate is: ", plate_gen_or_check(feat, vehicle), sep="")
            print("Press Space to continue!")
            keyboard.wait("space")

        elif feat == '1':
            print("_" * 50, "\n*Examples for accepted input: 29A1-21321 or 29A1 21321.",
            "- Note 1: The seri (the letter) is AA (or AB) for motorbike having engine's volume fewer than 50 cm^3.",
            "- Note 2: The first two number range from 10 to 99.", "_" * 50,
            sep="\n")
            try:
                if (plate := input("**Your desired plate: ").strip()).lower() == "esc":
                    sys.exit("Successfully exit the program.")
                if plate_gen_or_check('1', vehicle, plate):
                    print("\n____This is a valid plate!____")
                    print("Press Space to continue!")
                    keyboard.wait("space")
            except ValueError:
                print("\n____This is an invalid plate!____\n*Please check your city number and SERI!\n")
                print("Press Space to continue!")
                keyboard.wait("space")

        elif feat == "2":
            print("\n", "_" * 25, "Price", "_" * 25, sep="")
            print(regis_fee(vehicle))
            print("Press Space to continue!")
            keyboard.wait("space")

        elif feat == "3":
            print("\n", "_" * 20, "Details", "_" * 20, sep="")
            print(f"- User: {name}\n- Date of birth: {dob}\n- Type of vehicle: {_vehicle.capitalize()}\n\n{vehicle}")
            print("Press Space to continue!")
            keyboard.wait("space")

        else:
            print("*Please enter a number!\n")
            print("Press Space to continue!")
            keyboard.wait("space")

def plate_gen_or_check(index, vehicle, plate="29AA-51935") -> str|bool:
    """Return a license plate or check whether a license plate is valid

    Args:
        index (str): decide which mode the function would work (0 or 1)
        vehicle (Car or Motorbike): the class of the registered vehicle
        plate (str, optional): The plate number to check.
                            Defaults to "29AA-51935". (the dash - can be replaced by a space)

    Raises:
        ValueError: if the plate isn't valid.
    Returns:
        str: the license plate num (mode 0)
        bool: for checking the plate (mode 1)
    """
    # Format XXY-ZZZZZ where XX is a number from 11 to 99, Y is a letter (or AA/AB)
    if index == "0":  # Randomize the plate number
        nums = str(rd.randint(0, 99999))
        if (type(vehicle) is Motorbike) and (vehicle.checked()):
            additional_seri = rd.randint(1,9)
        else:
            additional_seri = ""
        plate_nums = '0' * (5 - len(nums)) + nums
        if (type(vehicle) is Motorbike) and (not vehicle.checked()):
            seri = rd.choice(["AA", "AB"])
        else:
            seri = rd.choice(Vehicle.SERI)
        city_num = rd.choice(Vehicle.CITIES[vehicle.city])
        return f"{city_num}{seri}{additional_seri}-{plate_nums}"

    elif index == "1":  # Check the wanted plate
        if regis_plate := re.search(r"(^[1-9][0-9])([a-z](?:[1-9]|[ab])?)(?:-| )[0-9]{5}$", plate.strip(), flags=re.IGNORECASE):
            if regis_plate.group(1) == "10":
                raise ValueError("Not a valid city number!")
            if regis_plate.group(1) not in Vehicle.CITIES[vehicle.city]:  # Valid number corresponding to the city
                raise ValueError("Not a valid city!")
            # Check for motorbike
            if type(vehicle) is Motorbike:
                # Check for other motorbikes
                if len(regis_plate.group(2)) != 2:
                    raise ValueError("Not a valid seri!")
                # Check for motorbikes with 50 cm^3 engine's volume
                elif vehicle.checked() and regis_plate.group(2).upper() in ["AA", "AB"]:
                    raise ValueError("Not a valid seri!")
                elif regis_plate.group(2) not in ["AA", "AB"] and (not vehicle.checked()):
                    raise ValueError("Not a valid seri!")
                else:
                    return True
            # Check for car
            else:
                if len(regis_plate.group(2)) != 1 and type(vehicle) is Car:
                    raise ValueError("Not a valid seri!")
                else:
                    return True
        else:
            raise ValueError("Not a valid plate!")

    else:
        print("Please enter 0 or 1!")
        return False


def check_age(dob: str) -> bool:
    """Validate the age of the user
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


def regis_fee(vehicle: Car|Motorbike) -> str:
    """Get the price (include components) of the vehicle
    
    Args:
        vehicle (Car|Motorbike): the type of vehicle (car or motorbike) 

    Returns:
        str: the formated table that show the total price and all components of the price of the vehicle
    """
    if type(vehicle) is Car:
        # Get the components
        if vehicle.city in Car.TAX_REGIS_PER.keys():
            veh_regis_fee = Car.TAX_REGIS_PER[vehicle.city]
        else:
            veh_regis_fee = 0
        if vehicle.city in Car.TAX_PLATE_REGIS:
            plate_fee = Car.TAX_PLATE_REGIS[vehicle.city]
        else:
            plate_fee = 42.67

        # Get the total price
        if vehicle.city not in Car.TAX_REGIS_PER.keys():
            tot = f"{vehicle.price * 1.1 + {plate_fee}:.2f}"
        elif vehicle.city in Car.TAX_REGIS_PER.keys() and vehicle.city not in Car.TAX_PLATE_REGIS.keys():
            tot = f"{vehicle.price * (1.1 + Car.TAX_REGIS_PER[vehicle.city]) + {plate_fee}:.2f}"
        elif vehicle.city == "Hanoi" or vehicle.city == "Ho Chi Minh City":
            tot = f"{vehicle.price * (1.1 + Car.TAX_REGIS_PER[vehicle.city]) + Car.TAX_PLATE_REGIS[vehicle.city]:.2f}"

    if type(vehicle) is Motorbike:
        # Get the components
        if vehicle.price < 639.66:
            plate_fee = 31.98
        elif 1705.76 >= vehicle.price >= 639.66:
            plate_fee = 63.97
        else:
            plate_fee = 127.93
        veh_regis_fee = 0

        # Get the total price
        if float(vehicle.price) < 639.66:
            tot = f"{vehicle.price * 1.1 + 31.98:.2f}"
        elif 1705.76 >= float(vehicle.price) >= 639.66:
            tot = f"{vehicle.price * 1.1 + 63.97:.2f}"
        else:
            tot = f"{vehicle.price * 1.1 + 127.93:.2f}"

    table = [["Original price", f"${vehicle.price:.2f}"], ["VAT Tax (10%)", f"${vehicle.price * 0.1:.2f}"],
            [f"Registrating fee ({veh_regis_fee:.1%})", f"${vehicle.price * veh_regis_fee:.2f}"],
            ["Plate registration fee", f"${plate_fee:.2f}"], ["Total", f"${tot}"]]
    return tabulate(table, headers=["Price Component", "Value"], tablefmt="grid", numalign="center")


if __name__ == "__main__":
    main()
