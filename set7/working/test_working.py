from working import convert
import pytest as pt


def test_correct():
    assert convert("9:34 AM to 3 PM") == "9:34 to 15:00"
    assert convert("9 AM to 5:45 PM") == "9:00 to 17:45"
    assert convert("9:34 AM to 3:45 PM") == "9:34 to 15:45"
    assert convert("9 AM to 3 PM") == "9:00 to 15:00"
    # 3 out of 4 assertions will fail if we don't account for the 9 AM to 5PM format and change it to 9:00 and 17:00


def test_correct_1():
    assert convert("9 PM to 1:30 AM") == "21:00 to 1:30"
    assert convert("8:45 PM to 12:45 AM") == "20:45 to 00:45"
    assert convert("8 PM to 12 AM") == "20:00 to 00:00"
    # Two last assertions will fail if we don't convert 12:xx AM to 00:xx.


def test_wrong_format():
    with pt.raises(ValueError):
        convert("cat")
        convert("9 AM - 12 PM")
        convert("13 PM to 12 AM")
        convert("12:60 AM to 5 AM")
        # The appropriateness of the minute part is covered by the regex
        # The regex make sure there must be a "to" in the string literal.
