def get_min(*args):
    if len(args) == 1:
        args = args[0]
    smallest_number = None
    for i in args:
        if smallest_number is None or i < smallest_number:
            smallest_number = i

    return smallest_number


def get_max(*args):
    if len(args) == 1:
        args = args[0]
    largest_number = None
    for i in args:
        if largest_number is None or i > largest_number:
            largest_number = i

    return largest_number


def get_second_highest_value(numbers):
    if len(numbers) < 2:
        return None
    highest_value = None
    second_highest_value = None
    for i in numbers:
        if highest_value is None or i > highest_value:
            highest_value = i
            continue
    for i in numbers:
        if second_highest_value is None or i > second_highest_value:
            if i != highest_value:
                second_highest_value = i
    return second_highest_value
