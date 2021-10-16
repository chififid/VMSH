from math import sqrt, fabs


# 1
def print_max_number(numbers):
    max_number = max(numbers)
    print(max_number)
    return max(numbers)


# 2
def no_null(number):
    if number == 0:
        return 1
    return number

def is_triangle(points):
    if (fabs(points[0][0] - points[1][0])) / no_null(fabs(points[0][1] - points[1][1])) != \
            (fabs(points[0][0] - points[2][0])) / no_null(fabs(points[0][1] - points[2][1])):
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
