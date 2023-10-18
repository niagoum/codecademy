

## write by niagoum
def separate(arr):
    res = []
    left_arr, right_arr = [], []
    for i in range(1, len(arr)):
        left_arr.append(arr[i]) if arr[i] < arr[0] else right_arr.append(arr[i])
    if left_arr:
        res.append(left_arr)
    res.append(arr[0])
    if right_arr:
        res.append(right_arr)
    return res
def quick(arr):
    l = len(arr)
    arr = separate(arr)
    arr_i = []
    while True:
        con = 0
        for i in arr:
            if not isinstance(i, list):
                arr_i.append(i)
                con += 1
            elif len(i) == 1:
                con += 1
                arr_i.append(i[0])
            else:
                arr_i += separate(i)
        if con == l:
            return arr_i
        arr = arr_i
        arr_i = []

## write by niagoum (recursive)
def quick_r(arr):
    if not arr:
        return [None] if not arr else None
    if len(arr) == 1:
        return [arr[0]]
    res, left_arr, right_arr = [], [], []
    for i in range(1, len(arr)):
        left_arr.append(arr[i]) if arr[i] < arr[0] else right_arr.append(arr[i])
    if left_arr:
        res += quick_r(left_arr)
    res.append(arr[0])
    if right_arr:
        res += quick_r(right_arr)
    return res

def quick_p(list):
    def f(list, start, end):
        if start >= end:
            return
        p = start
        for i in range(start, end):
            if list[i] < list[end]:
                list[i], list[p] = list[p], list[i]
                p += 1
        list[end], list[p] = list[p], list[end]
        f(list, start, p - 1)
        f(list, p + 1, end)
    f(list, 0, len(list)-1)
    return list



