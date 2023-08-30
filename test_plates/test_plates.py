
from plates import is_valid

def test_01():
    assert is_valid("A") == False

def test_02():
    assert is_valid("ASDCSDCSDC") == False


def test_06():
    assert is_valid("AA") == True

def test_06():
    assert is_valid("A2") == False


def test_04():
    assert is_valid("CS05") == False


def test_05():
    assert is_valid("PI3.14") == False




def test_07():
    assert is_valid("CS50P2") == False

