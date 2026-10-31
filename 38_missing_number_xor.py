def find_missing_number(numbers):
    result = 0
    for n in range(1, len(numbers)+2): result ^= n
    for n in numbers: result ^= n
    return result
