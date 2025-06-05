from math import floor


def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if is_perfect(number):
        return "perfect"
    elif is_abundant(number):
        return "abundant"
    else:
        return "deficient"

def is_perfect(number):
    return sum(get_factors(number)) == number

def is_abundant(number):
    return sum(get_factors(number)) > number

def is_deficient(number):
    return sum(get_factors(number)) < number

def get_factors(number):
    factors = []

    for i in range(1, floor(number / 2) + 1):
        if number % i == 0:
            factors.append(i)

    return factors