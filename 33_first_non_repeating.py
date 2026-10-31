def first_non_repeating(text):
    return next((c for c in text if text.count(c) == 1), None)
