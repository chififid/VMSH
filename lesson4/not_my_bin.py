def bin_search(l,x):
    left = 0
    right = len(l) - 1
    pos = -1
    while pos == -1 and (left<=right):
        mid = (right + left)//2
        if l[mid] == x:
            pos = mid
        elif l[mid]>x:
            right = mid -1
        else:
            left = mid + 1
    return pos