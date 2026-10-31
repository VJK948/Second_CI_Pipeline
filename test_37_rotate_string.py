import importlib
module = importlib.import_module("37_rotate_string")

def test_case_1():
    assert module.rotate_string("abcdef", 2) == "efabcd"

def test_case_2():
    assert module.rotate_string("", 3) == ""

