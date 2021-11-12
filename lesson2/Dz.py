# 1
def input_numbers():
    line = "Введите числа через пробел: "
    numbers_str = input(line).split(' ')
    return [int(num) for num in numbers_str]


def middle_num(numbers):
    summa = 0
    for num in numbers:
        summa += num
    return summa/len(numbers)


# 2
def middle_num_rec(count=0):
    line = "Введите число(0 - конец ввода): "
    number = int(input(line))
    count,  result = 0, 0

    while number != 0:
        result += number
        count += 1
        number = int(input(line))

    return result / count

# 3
def alternation_lists_re(*lists):
    if [] in lists:
        return []
    result = []

    for i in range(len(lists)):
        result += [(lists[i][0])]
        lists[i].pop(0)

    return result + alternation_lists_re(*lists)


# 4
def max_min(numbers):
    result = {"min": numbers[0], "max": numbers[0]}

    for num in numbers:
        if num < result["min"]:
            result["min"] = num
        elif num > result["max"]:
            result["max"] = num

    return result


# 5
def max_increasing_part(numbers):
    result = {"from": 0, "to": 0, "len": 1}

    i = 0
    while i < len(numbers):
        for g in range(i + 1, len(numbers)):
            if numbers[g] <= numbers[g - 1]:
                break

            if g - i + 1 > result["len"]:
                result["from"] = i
                result["to"] = g + 1
                result["len"] = g - i + 1

        i = max(result["to"], i + 1)

    if result["len"] <= 1:
        result = 0
    return result
