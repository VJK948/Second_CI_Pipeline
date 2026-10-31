import importlib
module = importlib.import_module("39_transpose_matrix")

def test_case_1():
    assert module.transpose_matrix([[1,2],[3,4]]) == [[1,3],[2,4]]

def test_case_2():
    assert module.transpose_matrix([]) == []

