from numb3rs import validate


def test_proper_ipv4():
    assert validate("123.24.3.4") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True


def test_str():
    assert validate("256.3.45.100") == False
    assert validate("1.34.150.1000") == False
    assert validate("cat") == False
    assert validate("cat.dog.cow.bird") == False
    assert validate("cat.3.4.5") == False
    assert validate("2 .3.4 .5") == False
    assert validate("2.333.433.533") == False
