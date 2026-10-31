import importlib
module = importlib.import_module("31_pangram")

def test_case_1():
    assert module.is_pangram("The quick brown fox jumps over the lazy dog") == True

def test_case_2():
    assert module.is_pangram("Hello") == False

