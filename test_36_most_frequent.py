import importlib
module = importlib.import_module("36_most_frequent")

def test_case_1():
    assert module.most_frequent([1,3,3,2]) == 3

def test_case_2():
    assert module.most_frequent([]) == None

