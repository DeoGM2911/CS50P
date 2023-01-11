from plates import is_valid


def test_req_1():
    for plate in ["helloworld", "x", ""]:
        assert is_valid(plate) is False


def test_req_2():
    for plate in ["23Hel2", "C3", "3C"]:
        assert is_valid(plate) is False
    
    
def test_req_4():
    for plate in ["CS@23", "CS.3", "CS,4"]:
        assert is_valid(plate) is False


def test_req_3():
    for plate in ["CS05", "CS50P", "CS2D9", "CS23C2", "CS5P"]:
        assert is_valid(plate) is False