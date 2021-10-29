# 1
def evc(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


# 2
def evc_max(*nums):
    if len(nums) < 1:
        return False
    elif len(nums) == 1:
        return nums[0]

    return evc_max(*[evc(nums[0], nums[1]), *nums[2:]])
