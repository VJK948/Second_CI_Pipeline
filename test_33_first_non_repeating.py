import importlib
module = importlib.import_module("33_first_non_repeating")

def test_case_1():
    assert module.first_non_repeating("aabbcdd") == "c"

def test_case_2():
    assert module.first_non_repeating("aabb") == None

