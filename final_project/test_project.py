from project import check_age, regis_fee, plate_gen_or_check
import pytest as pt
from vehicle import Car, Motorbike


def test_plate_gen_or_check():
    # Check mode 1
    m = Motorbike(125, "600", None, None, None, city="Hanoi")
    m1 = Motorbike(50, "600", None, None, None, city="Hanoi")
    cr = Car(800, '10000', None, None, None, None, city="Hanoi")
    assert plate_gen_or_check("1", m, "30M-12344") is True
    assert plate_gen_or_check("1", m1, "30AA-12344") is True
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
    c = Car(800, '10000', None, None, None, None, city="Hanoi")
    m = Motorbike(125, "600", None, None, None, city="Ho Chi Minh City")
    assert regis_fee(c) == "Total: $13053.33"
    assert regis_fee(m) == "Total: $691.98"


def test_check_age():
    assert check_age("29/11/2004") is False
    assert check_age("31-12-2000") is False
    assert check_age("1-1-2010") is True
    with pt.raises(ValueError):
        check_age("September 21, 2000")
        check_age("21-32-2003")
        check_age("cat")
