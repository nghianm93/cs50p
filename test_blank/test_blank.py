from bank import value

def test_hello():
    assert value("hello") == 0


def test_start_with_h():
    assert value("haha") == 20


def test_else():
    assert value("") == 100

def test_start_with_H():
    assert value("Haha") == 20