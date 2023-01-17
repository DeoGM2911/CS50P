import re
from datetime import date
from vehicle import Car, Motorbike
import sys
import argparse


def main():
    pass


def plate_gen_or_check(plate, ):
    pass


def check_age(dob):
    today = date.today()
    pass


def regis_fee(vehicle, prc, city):
    """Get the total price include tax of the vehicle
    
    Args:
        vehicle (str): the type of vehicle (car or motorbike) 
        prc (float): the price of the vehicle (tax not included) 
        city (str): the name of the city where the vehicle is bought 

    Returns:
        str: the formated string that show the total price of the vehicle
    """
    if vehicle.strip().lower() == "car":
        return Car(0, 0, prc, city=city).get_tot_price_car()  # Only the price and city are needed so other params are 0
    if vehicle.strip().lower() == "motorbike":
        return Motorbike(0, 0, prc).get_tot_price_motorbike()  # Only the price is needed so other params are 0