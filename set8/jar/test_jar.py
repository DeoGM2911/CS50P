from jar import Jar
import pytest as pt


def test_init():
    jar = Jar(20)
    assert (jar.capacity, jar.size) == (20, 0)
    with pt.raises(ValueError):
        jar = Jar(-12)


def test_str():
    jar = Jar(20)
    assert str(jar) == ""
    jar.deposit(10) 
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(8)
    assert str(jar) == "🍪🍪"


def  test_deposit():
    jar = Jar(20)
    jar.deposit(12)
    assert jar.size == 12
    with pt.raises(ValueError):
        jar.deposit(-12)


def test_withdraw():
    jar = Jar(20)
    jar.deposit(15)
    jar.withdraw(12)
    assert jar.size == 3
    with pt.raises(ValueError):
        jar.withdraw(-12)
