import random
import time
from not_my_bin import bin_search
from not_my_merge_sort import merge_sort


def bin_rec(nums, x, pos=0):
    if nums[0] > x or nums[-1] < x:
        return -1

    md = len(nums) // 2
    new_pos = pos + md

    if nums[md - 1] < x:
        return bin_rec(nums[md:], x, new_pos)
    elif nums[md - 1] > x:
        return bin_rec(nums[:md - 1], x, pos)
    else:
        return new_pos


def gnome_sort(nums):
    i = 0
    j = 0

    while i < len(nums) - 1:
        if nums[i] <= nums[i + 1]:
            if j > i:
                i = j

            i += 1

        else:
            middle_num = nums[i + 1]
            nums[i + 1] = nums[i]
            nums[i] = middle_num

            if i > j:
                j = i

            if i > 0:
                i -= 1

    return nums


def default_sort(data):
    return data.sort()


def check_speed(func, data):
    start = time.time()
    func(*data)
    end = time.time()
    print(end - start)


big_data = []

for _ in range(10000):
    big_data.append(random.random())

check_speed(gnome_sort, [big_data])  # +- 8.6 секунд
check_speed(merge_sort, [big_data])  # +- 0.02 секунды
check_speed(default_sort, [big_data])  # +- 0.00003 секунды


x = random.random()
big_data = [x]

for i in range(1000000):
    big_data.append(random.random() + i)
big_data.append(x)

check_speed(bin_rec, [big_data, x])  # 0.0004
check_speed(bin_search, [big_data, x])  # 0.000005
'''
Разрыв между рукурсивной сортировкой и не рекурсивной сильно увеличивается
при увелечении входного массива относительно егор длинны
'''
