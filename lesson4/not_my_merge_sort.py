def merge(l, r):
    res = []
    i = 0
    j = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    res += l[i:]
    res += r[j:]

    return res


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    elif len(arr) > 1:
        mid = len(arr) // 2
        Left = arr[:mid]
        Right = arr[mid:]
        Left = merge_sort(Left)
        Right = merge_sort(Right)

        return merge(Left, Right)