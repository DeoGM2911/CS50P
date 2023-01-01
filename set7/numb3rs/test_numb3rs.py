from numb3rs import validate


def test_proper_ipv4():
    for ip in ["123.24.3.4", "0.0.0.0", "255.255.255.255"]:
        assert validate(ip) == True


def test_str():
    for ip_str in ["256.3.45.100", "1.34.150.1000", "cat", "cat.dog.cow.bird", "cat.3.4.5", "", "\n", "2 .3.4 .5"]:
        assert validate(ip_str) == False
