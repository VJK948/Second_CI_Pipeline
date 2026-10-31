import importlib
module = importlib.import_module("40_gcd")

def test_case_1():
    assert module.gcd(12,18) == 6

def test_case_2():
    assert module.gcd(7,0) == 7

