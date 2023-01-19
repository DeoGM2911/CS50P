from project import plate_gen_or_check, regis_fee, check_age
import pytest as pt
from vehicle import Car, Motorbike


def test_plate_gen_or_check():
    pass


def test_regis_fee():
    # get_tot_price_car() and get_tot_price_motorbike() have been tested in test_vehicle.py
    c = Car(0, '10000', None, None, None, None, city="Hanoi")
    m = Motorbike(0, "5000", None, None, None, city="Ho Chi Minh City")
    assert regis_fee("car", '10000', "Hanoi") == '$13053.33'
    assert regis_fee("motorbike", '5000', "Ho Chi Minh City") == m.get_tot_price_motorbike()

def test_check_age():
    assert check_age("29/11/2004") is False
    assert check_age("31-12-2000") is False
    assert check_age("1-1-2010") is True
    with pt.raises(ValueError):
        check_age("September 21, 2000")
        check_age("21-32-2003")
        check_age("cat")
