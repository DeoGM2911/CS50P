# **Vplate**

## 1. **Video Demo**:  <URL HERE>

### 2. **Description**

#### 2.1 *Overview*

- The project's name is Vplate, which stands for Vehicle's plate and Viet plate. The name was inspired by the license plate system in my home country Vietnam.
- The project's aims are to create a program that:
  - Help users **check their desired license plate** (*in reality, Vietnam doesn't allow this; however, inspired by the plate problem in problem set 2, I decided to add this feature so that anyone can have their wanted plate*).
  - ***Randomly*** **generate one** for them (if they don't have a desired plate).
  - **Printing** out **the users' and their vehicles' details** (after they've inputted their information).
  - **Printing** the **price of buying and registrating the vehicle** (also show the price components).
  - In the process of inputting data, the program also **checks whether the user is 18 year old**. (*in Vietnam, the minimal age to buy a vehicle legally is 18*)
- The license plate in Vietnam obeys the following rules:
  - Need to have a city number (*Example: **29**AA-51935. In this case, it is the bold number*). The city number range from 11 to 99 (*Notes: not all number is accounted. For example: 80 is not include in the program as it represents vehicle used by the governments*)
  - Need to have a seri (*Example: 29**AA**-51935. In this case, it is the bold letters*). The seri for motorbike having **engine's volume over 50 cm^3** is exactly **one letter** in the alphabet **combine** with a number from 1 to 9 (Example: 30**M1**-28451). On the other hand, vehicle with engine having volume **less than or equal to 50 cm^3** would have the seri of **"AA"** or **"AB"**. Cars' license plates' seri is exactly **one letter** in the alphabet.
  - Need to end with **exactly 5 numbers** (*could be any number ranging from 00000 to 99999*)
  - Need to have a dash(-) or a whitespace as the seperator between the seri and the ending numbers (*Example: 29AA-51935 or 29AA 51935 are accepted*)

#### 2.2 *Details about the program*

##### 2.2.1 The classes used in the program

- Inside the program, a class named **Vehicle** is implemented along with the **Car** and **Motorbike** class which **inherit the Vehicle class**. The class Vehicle has the following attributes:
  - The **engine's volume** in cm^3 (of type float)
  - The **original price** (tax not inlcuded) in USD (of type float)
- Each of the mentioned above attributes has a *getter* and *setter* to check for valid argument.

##### **The initialization of Vehicle, Car, and Motorbike:*

``` Python
def __init__(self, cyl_capacity: float|int, price: float|int, city: str="Hanoi") -> None:
    self.cyl_capacity = cyl_capacity  
    self.price = price  
    self.city = city
```

##### **The setter and getter of both properties:*

``` Python
@property
    def cyl_capacity(self):
        return self._cyl_capacity
    
@cyl_capacity.setter
def cyl_capacity(self, cyl_capacity):
    if float(cyl_capacity) < 0:
        raise ValueError("Not a valid number!")
    self._cyl_capacity = cyl_capacity
```

- *Car* and *Motorbike* (or *Vehicle*) also have *class constants*:
  - Vehicle's class constant:
    - CITIES - a dictionary containing Vietnamese cities and their corresponding city number(s) on the license plate.
    - SERI - a list containing all the series (*except for **AA** and **AB***) needed for generating or checking a license plate.
  - Car's class constants:
    - TAX_PLATE_REGIS: a dictionary containing the plate registrating fee in Hanoi and Ho Chi Minh city. Other cities/provinces have registrating fee equal to $42.67
    - TAX_REGIS_PER: a dictionary with the percentage of the original price of the vehicle that the user need to pay on top of the original price while registrating the vehicle. Cities that aren't in the dictionary have a fee of $0.

- A \_\_str__() method is also defined. str(vehicle) is a string with data about the vehicle in a table format supported by the tabulate module.

``` Python
def __str__(self):
    attrs = [["Engine's volume", f"{self.cyl_capacity:.2f cm^3"], ["Price", f"${self.price:.2f}"]]
    return f"""
________________The vehicle's attributes_______________
{tabulate(attrs, headers=["Attribute", "Value"], tablefmt="grid", numalign="center")}""".strip()
```

- In the class *Motorbike*, there is a method called checked() to see if the vehicle has over 50 cm^3 of engin's volume:

``` Python
def checked(self):
    return self.cyl_capacity > 50
```

**Notes 1**: Other attributes/properties of car and motorbikes weren't included as they are redundant in the program.
**Notes 2**: The class Car and Motorbike can actually be deleted as only 1 additional method is added. However, to explicitly distinguish the different taxes and fees that are implied on cars and motorbikes in Vietnam, I decided to create the two class *Car* and *Motorbike*  

##### 2.2.2 The functions implemented in the program

- Four functions are implemented in project.py.
  - **plate_gen_or_check**:
    - Randomly generating a license plate or checking whether a plate is valid.
    - Take 3 arguments:
      - index (str): decide which mode the function would work (0 or 1)
      - vehicle (Car or Motorbike): the class of the registered vehicle
      - plate (str, optional): The plate number to check.
            Defaults to "29AA-51935".
    - Raises: ValueError if the plate isn't valid.
    - Returns:
      - str: the license plate (mode 0)
      - bool: for checking the plate (mode 1)
  - **check_age**:
    - Check whether the user is old enough to buy a car/motorbike.
    - Take 1 argument: dob (str): the date of birth. Accepted format: DD/MM/YYYY or DD-MM-YYYY
    - Returns a boolean: False if the user age is qualified
  - **regis_fee**:
    - Return a string in form of a table to show the total price along with the components needed to pay while buying a vehicle.
    - Take 1 argument: vehicle (Car|Motorbike): the type of vehicle (car or motorbike)
    - Returns a str: the formated table that show the total price and all components of the price of the vehicle
  - **main**:
    - Take 0 arguments
    - Prompt the user for:
      - His/her name.
      - His/her date of birth (*in Vietnamese format DD-MM-YYYY or DD/MM/YYYY. If the user's age is less than 18, the program will exit via sys.exit*).
      - His/her registrating city. (*If it isn't a Vietnamese cities or provinces, the program would reprompt!*)
      - His/her vehicle's engine's volume and price (*reprompt if the user input invalid number*).
    - After that, it creates a menu with 4 features for the user to choose:
      - Randomly generate a license plate.
      - Check a desired license plate.
      - See the price of his/her vehicle.
      - See the details about him/her and his/her vehicle.
      - Exit the program.
    - The user can type in "esc" case-insensitively to exit the program while being prompted.
    - (**) indicates an answer is required.

#### 2.3 *Details about test_project.py*

- The file contains 6 tests:
  - **test_init**: test the initialization of the classes *Car* and *Motorbike* (*expected to raise a ValueError in inappropriate arguments).
  - **test_str**: test the str version of *Car* and *Motorbike*.
  - **test_checked**: test the checked() method of the class *Motorbike* (True if the engine's volume is larger than 50 cm^3).
  - **test_plate_gen_or_check**: test the two mode (0 and 1) of the function *plate_gen_or_check* and check if the function raises a ValueError if the plate is invalid in mode 1.
  - **test_check_age**: test whether the function check_age() gives True if the user is less than 18 years old and raise a ValueError if the dob argument is wrong.
