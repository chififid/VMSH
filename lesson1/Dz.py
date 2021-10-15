from math import sqrt


# 1
def print_max_number(numbers):
    max_number = max(numbers)
    print(max_number)
    return max(numbers)


# 2
def is_triangle(points):
    planes = [[point[0] for point in points], [point[1] for point in points]]

    if len(set(planes[0])) > 1 and len(set(planes[1])) > 1:
        return True

    return False


# 3
def find_roots_in_square_case(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return False
    elif discriminant == 0:
        return (-b) / (2 * a)
    else:
        root_1 = ((-b) + sqrt(discriminant)) / (2 * a)
        root_2 = ((-b) - sqrt(discriminant)) / (2 * a)
        return [root_1, root_2]
