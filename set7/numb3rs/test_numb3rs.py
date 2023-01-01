from numb3rs import validate


def test_proper_ipv4():
    for ip in ["123.24.3.4", "0.0.0.0", "255.255.255.255"]:
        assert validate(ip) == True


def test_str():
    for ip_str in ["cat", "cat.dog.cow.bird", "cat.3.4.5", "", "\n"]:
        assert validate(ip_str) == False
