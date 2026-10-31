def move_zeros(numbers):
    return [x for x in numbers if x != 0] + [x for x in numbers if x == 0]
