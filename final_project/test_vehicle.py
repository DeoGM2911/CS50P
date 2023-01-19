from vehicle import Car, Motorbike, Vehicle
import pytest as pt


def test_init():
    with pt.raises(ValueError):
        Car("two hundred", 21312, None, None, None, None)
        Car(23, 21312, None, None, None, None, "two")
        Car(23, 21321, None, None, None, None, city="Hanover")
        Motorbike(50, "three thousand", None, None, None)
        Motorbike(125, 21321, "eleven thousand", None, None)


def test_str():
    car = Car(300, 21312, None, None, None, None)
    assert str(car) == f"""
* Note: if the value is None, it means that you haven't provided the info.
*** The vehicle's attributes are:
    - Power: {car.power} (HP)
    - Cylinder's Volume: {car.cyl_capacity} (cm^3)
    - Max torsion: {car.max_tor} (rounds/min)
    - Mass: {car.mass} (tons)
    - Price: ${car.price}\n  - Capacity: {car.pass_capacity} people\n  - Max Load: {car.max_load} (tons)""".strip()


def test_checked():
    motor1 = Motorbike(125, 21321, None, None, None)
    motor2 = Motorbike(50, 21321, None, None, None)
    assert motor1.checked() is False
    assert motor2.checked() is True


def test_get_tot_price():
    car1 = Car(300, 21312, None, None, None, None)
    motor3 = Motorbike(125, 21321, None, None, None)
    assert car1.get_tot_price_car() == f"Total: ${float(car1.price) * (1.1 + Car.tax_regitration_fee[car1.city]) + Car.tax_plate_regitration[car1.city]:.2f}"
    assert motor3.get_tot_price_motorbike() ==  f"Total: ${float(motor3.price) * 1.1 + 127.93:.2f}"