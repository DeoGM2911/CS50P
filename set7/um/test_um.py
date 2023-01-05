from um import count


def test_start_or_end():
    assert count("um") == 1
    assert count("this is, Um") == 1
    assert count("UM?") == 1
    # All assertions here will fail if we don't add the whitespaces before and after the string
    # Of course in the case with my regular expression


def test_middle():
    assert count("This is, um..., amazing!") == 1
    assert count("hello, UM, world?") == 1


def test_word_with_um():
    assert count("yummy") == 0
    assert count("This is, um ..., an incredible album!")