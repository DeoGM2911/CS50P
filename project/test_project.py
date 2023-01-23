from project import Car, Motorbike
from project import plate_gen_or_check, check_age, regis_fee
import pytest as pt
from tabulate import tabulate


def test_init():
    with pt.raises(ValueError):
        Car("two hundred", 21312, "Hanoi")
        Car(23, 21312, "two")
        Car(23, 21321, city="Hanover")
        Motorbike(50, "three thousand")
        Car(-1, 2123)
        Car(321, -21321)


def test_str():
    car = Car(300, 21312)
    attrs = [["Engine's volume", f"{car.cyl_capacity:.2f} cm^3"], ["Price", f"${car.price:.2f}"]]
    assert str(car) == f"""
________________The vehicle's attributes_______________
{tabulate(attrs, headers=["Attribute", "Value"], tablefmt="grid")}""".strip()


def test_checked():
    motor1 = Motorbike(125, 21321)
    motor2 = Motorbike(50, 21321)
    assert motor1.checked() is True
    assert motor2.checked() is False


def test_plate_gen_or_check():
    # Check mode 1
    m = Motorbike(125, 600, city="Hanoi")
    m1 = Motorbike(50, 600, city="Hanoi")
    cr = Car(800, 10000, city="Hanoi")
    assert plate_gen_or_check("1", m, "30M-12344") is True
    assert plate_gen_or_check("1", m1, "30AA-12344") is True
    assert plate_gen_or_check("1", m, "30M 12344") is True
    with pt.raises(ValueError):
        plate_gen_or_check("1", m, "30AB-21321")
        plate_gen_or_check("1", m, "36A-25341")
        plate_gen_or_check("1", m, "21Q-321033")
        plate_gen_or_check("1", m, "10A-21301")
        plate_gen_or_check("1", cr, "32AB-21903")
    # Check mode 0
    plate = plate_gen_or_check("0", m1)
    assert "-" in plate
    assert plate[:2] in Motorbike.cities["Hanoi"]
    assert plate[2:4] in ["AA", "AB"]
    for letter in Motorbike.seri:
        assert letter not in plate[-5:]


def test_regis_fee():
    # get_tot_price_car() and get_tot_price_motorbike() have been tested in test_vehicle.py
    c = Car(800, 10000, city="Hanoi")
    m = Motorbike(125, 600, city="Ho Chi Minh City")
    table1 = [["Original price", "$10000.00"], ["VAT Tax (10%)", "$1000.00"],
            ["Registrating fee (12.0%)", "$1200.00"],
            ["Plate registration fee", "$853.33"], ["Total", "$13053.33"]]
    regis_fee(c) == tabulate(table1, headers=["Price Component", "Value"], tablefmt="grid", numalign="center")
    table2 = [["Original price", "$600.00"], ["VAT Tax (10%)", "$60.00"],
            ["Registrating fee (0.0%)", "$0.00"],
            ["Plate registration fee", "$31.98"], ["Total", "$691.98"]]
    regis_fee(m) == tabulate(table2, headers=["Price Component", "Value"], tablefmt="grid", numalign="center")


def test_check_age():
    assert check_age("29/11/2004") is False
    assert check_age("31-12-2000") is False
    assert check_age("1-1-2010") is True
    with pt.raises(ValueError):
        check_age("September 21, 2000")
        check_age("21-32-2003")
        check_age("cat")