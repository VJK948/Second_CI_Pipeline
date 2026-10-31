import importlib
module = importlib.import_module("32_count_words")

def test_case_1():
    assert module.count_words("Hello world") == 2

def test_case_2():
    assert module.count_words("") == 0

