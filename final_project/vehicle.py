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
        "Ho Chi Minh city": ['41', '50', '51', '52' ,'53', '54', '55', '56', '57', '58', '59'], "Thua Thien Hue": ['75'],
        "Tien Giang": ['63'], "Tra Vinh": ['84'], "Tuyen Quang": ['22'], "Vinh Long": ['64'], "Vinh Phuc": ['88'], "Yen Bai": ['21']
    }
    
    seri = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L', 'M', 'N', 'P', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    
    def __init__(self, cyl_capacity, price, max_torsion, mass, power, city="Hanoi") -> None:
        self.cyl_capacity = cyl_capacity  # the vehicle's engine's capacity in cm^3
        self.price = price  # tax-not-included price in USD
        self.max_tor = max_torsion  # the maximum torsion of the vehicle in rounds/min
        self.mass = mass  # The vehicle's mass in kg
        self.power = power  # The vehicle's power in Horse Power or HP
        self.city = city
    
    def __str__(self):
        return f"""
* Note: if the value is None, it means that you haven't provided the info.
*** The vehicle's attributes are:
    - Power: {self.power} (HP)
    - Capacity: {self.cyl_capacity} (cm^3)
    - Max torsion: {self.max_tor} (rounds/min)
    - Mass: {self.mass} (tons)
    - Price: ${self.price}""".strip()
    
    def __add__(self, object):
        return f"The total price is: ${self.price + object.price}"
    
    @property
    def power(self):
        return self._power
    
    @power.setter
    def power(self, power):
        if power is None:
            pass
        elif float(power) < 0:
            raise ValueError("Not a valid number!")
        self._power = power
    
    @property
    def cyl_capacity(self):
        return self._cyl_capacity
    
    @cyl_capacity.setter
    def cyl_capacity(self, cyl_capacity):
        if float(cyl_capacity) < 0:
            raise ValueError("Not a valid number!")
        self._cyl_capacity = cyl_capacity
    
    @property
    def max_tor(self):
        return self._max_torsion
    
    @max_tor.setter
    def max_tor(self, max_torsion):
        if max_torsion is None:
            pass
        elif float(max_torsion) < 0:
            raise ValueError("Not a valid number!")
        self._max_torsion = max_torsion
    
    @property
    def mass(self):
        return self._mass
    
    @mass.setter
    def mass(self, mass):
        if mass is None:
            pass
        elif float(mass) < 0:
            raise ValueError("Not a valid number!")
        self._mass = mass
    
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
    
    def checked(self):  # Mostly used by the motorbike subclass
        return float(self.cyl_capacity) <= 50


class Car(Vehicle):
    tax_plate_regitration = {"Hanoi": 853.33, "Ho Chi Minh City": 469.33}  # other cities/provinces correspond to $42.67
    tax_regitration_fee = {"Hanoi": 0.12, "Danang": 0.12, "Haiphong": 0.12, "Ho Chi Minh City": 0.1, "Cantho": 0.1}
    # the VAT tax is 10% for all products
    
    def __init__(self, cyl_capacity, price, max_torsion, mass, power, max_load, pass_capacity=4, city="Hanoi"):
        super().__init__(cyl_capacity, price, max_torsion, mass, power, city)
        self.pass_capacity = pass_capacity  # The maximum passengers the car can have
        self.max_load = max_load  # The maximum load in tons
    
    def __str__(self):
        return f"{super().__str__()}\n  - Capacity: {float(self.pass_capacity)} people\n  - Max Load: {float(self.max_load)} (tons)"
    
    @property
    def pass_capacity(self):
        return self._pass_capa
    
    @pass_capacity.setter
    def pass_capacity(self, pass_capacity):
        if float(pass_capacity) < 2:
            raise ValueError("Not a valid capacity!")
        self._pass_capa = pass_capacity
    
    @property
    def max_load(self):
        return self._max_load
    
    @max_load.setter
    def max_load(self, max_load):
        if max_load is None:
            pass
        elif float(max_load) < 0:
            raise ValueError("Not a valid number!")
        self._max_load = max_load
    
    def get_tot_price_car(self):
        if self.city not in Car.tax_regitration_fee.keys():
            return f"Total: ${float(self.price) * 1.1 + 42.67}"
        elif self.city in Car.tax_regitration_fee.keys() and self.city not in Car.tax_plate_regitration.keys():
            return f"Total: ${float(self.price) * (1.1 + Car.tax_regitration_fee[self.city]) + 42.67}"
        elif self.city == "Hanoi" or self.city == "Ho Chi Minh City":
            return f"Total: ${float(self.price) * (1.1 + Car.tax_regitration_fee[self.city]) + Car.tax_plate_regitration[self.city]}"

    def type_of_car(self):
        if 2 <= float(self.pass_capacity) <= 7:
            return "Family car"
        elif 7 >= float(self.mass) >= 3:
            return "Light commercial vehicle"
        elif float(self.mass) > 7:
            return "Heavy truck"


class Motorbike(Vehicle):
    def __init__(self, cyl_capacity, price, max_torsion, mass, power, city="Hanoi") -> None:
        super().__init__(cyl_capacity, price, max_torsion, mass, power, city)
    
    def __str__(self):
        return super().__str__()
    
    def get_tot_price_motorbike(self):
        if float(self.price) < 639.66:
            return f"Total: ${float(self.price) * 1.1 + 31.98}"
        elif 1705.76 >= float(self.price) >= 639.66:
            return f"Total: ${float(self.price) * 1.1 + 63.97}"
        else:
            return f"Total: ${float(self.price) * 1.1 + 127.93}"
    
    def type_motor(self):
        return float(self.cyl_capacity) > 50
