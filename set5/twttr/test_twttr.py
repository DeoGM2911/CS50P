from twttr import shorten


def test_str():
    assert shorten("Straight") == "Strght"


def test_num():
    assert shorten("-2.0") == "-2.0"


def test_blank():
    assert shorten("") == ""
