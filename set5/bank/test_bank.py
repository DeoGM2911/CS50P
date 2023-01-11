from bank import value


def test_start_with_h():
    assert value("halo") == 20
    assert value("HAlo") == 20


def test_hello():
    assert value("hello") == 0
    assert value("HELlo my friend!") == 0


def test_other():
    for greet in ['xin chao', 'ni hao', 'bonjour', '']:
        assert value(greet) == 100
