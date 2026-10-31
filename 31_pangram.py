def is_pangram(text):
    return all(c in text.lower() for c in "abcdefghijklmnopqrstuvwxyz")
