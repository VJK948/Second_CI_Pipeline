import importlib
module = importlib.import_module("38_missing_number_xor")

def test_case_1():
    assert module.find_missing_number([1,2,4,5]) == 3

def test_case_2():
    assert module.find_missing_number([2,3,4]) == 1

