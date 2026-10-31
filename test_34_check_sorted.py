import importlib
module = importlib.import_module("34_check_sorted")

def test_case_1():
    assert module.is_sorted([1,2,2,4]) == True

def test_case_2():
    assert module.is_sorted([3,1]) == False

