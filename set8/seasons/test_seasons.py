from seasons import sing, get_dob
from datetime import date
today = date.today()

def test_sing():
    assert sing("0") == "Zero"
    assert sing("123546") == "One hundred twenty-three thousand, five hundred forty-six"


def test_get_dob_correct():
    assert get_dob("2004-11-29", today) == (True, date(2004, 11, 29))
    assert get_dob("2000-12-31", today) == (True, date(2000, 12, 31))
    assert get_dob("0001-1-9", today) == (True, date(1, 1, 9))


def test_get_dob_wrong():
    assert get_dob("November 29th, 2004", today) == (False, None)
    assert get_dob("01/19/2004", today) == (False, None)
    assert get_dob("3000-09-3", today) == (False, None)
    assert get_dob("2000-13-2", today) == (False, None)
    assert get_dob("2000-12-32", today) == (False, None)
