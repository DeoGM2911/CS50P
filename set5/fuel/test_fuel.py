import pytest as pt
from fuel import convert, gauge


def test_convert_proper_arg():
    for frac, percent in {"0/1": 0, "1/2": 50, "9/9": 100, "2/3": 66}.items():
        assert convert(frac) == percent

def test_convert_wrong():
    with pt.raises(ZeroDivisionError):
        convert("2/0")
    with pt.raises(ValueError):
        convert("cat/dog")
    with pt.raises(ValueError):
        convert("4/3")        
        

def test_gauge():
    for per, out in {"E": 1, "F": 99, "50%": 50}.items():
        assert gauge(out) == per