import importlib
module = importlib.import_module("35_move_zeros")

def test_case_1():
    assert module.move_zeros([0,1,0,3]) == [1,3,0,0]

def test_case_2():
    assert module.move_zeros([1,2]) == [1,2]

