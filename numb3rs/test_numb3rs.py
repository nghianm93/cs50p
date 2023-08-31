
from numb3rs import validated


def test_numb3rs():
    assert validated("192.168.1.1") == True
    assert validated("0.0.0.0") == True
    assert validated("255.255.255.255") == True
    assert validated("10.20.30.40") == True
    assert validated("300.0.0.0") == False
    assert validated("192.168.1") == False
    assert validated("192.168.1.1.1") == False
    assert validated("192.168.-1.1") == False
    assert validated("abc.def.ghi.jkl") == False


if __name__ == "__main__":
    test_numb3rs()
    print("All tests passed!")