def most_frequent(numbers):
    return max(dict.fromkeys(numbers), key=numbers.count) if numbers else None
