from numb3rs_no_regex import validate_no_regex as v


def test_correct_ip():
    for ip in ["1.2.3.4", "0.0.0.0", "255.255.255.255"]:
        assert v(ip) == True


def test_str_ip():
    for ip_str in ["256.3.45.100", "1.34.150.1000", "cat", "cat.dog.cow.bird", "cat.3.4.5", "", "\n", "2 .3.4 .5"]:
        assert v(ip_str) == False



