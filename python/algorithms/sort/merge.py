import numpy as np
import random

def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


## divide once (no recursive)
def compare(arr_l, arr_r):
    res, i, j = [], 0, 0
    while True:
        if arr_l[i] < arr_r[j]:
            res.append(arr_l[i])
            i += 1
        else:
            res.append(arr_r[j])
            j += 1
        if i == len(arr_l):
            res += arr_r[j:]
            break
        if j == len(arr_r):
            res += arr_l[i:]
            break
    return res

def merge_m(arr):
    arr = [[i] for i in arr]
    while len(arr) != 1:
        arr_i = []
        if_odd = len(arr) % 2
        for i in range(0, len(arr) - if_odd, 2):
            arr_i.append(compare(arr[i], arr[i+1]))
        if if_odd:
            arr_i.append(arr[-1])
        arr = arr_i
    return arr[0]

## divide once (recursive)
def merge_m_r(arr):
    if not isinstance(arr[0], list):
        return merge_m_r([[i] for i in arr])
    if len(arr) == 1:
        return arr[0]
    arr_i = []
    if_odd = len(arr) % 2
    for i in range(0, len(arr) - if_odd, 2):
        arr_i.append(compare(arr[i], arr[i+1]))
    if if_odd:
        arr_i.append(arr[-1])
    arr = arr_i
    return merge_m_r(arr)

## two point divide (recursive)
def merge_r(arr):
    if len(arr) < 2:
        return arr
    index = len(arr) // 2

    arr_l = merge_r(arr[:index])
    arr_r = merge_r(arr[index:])

    res, i, j = [], 0, 0
    while True:
        if arr_l[i] < arr_r[j]:
            res.append(arr_l[i])
            i += 1
        else:
            res.append(arr_r[j])
            j += 1
        if i == len(arr_l):
            res += arr_r[j:]
            break
        if j == len(arr_r):
            res += arr_l[i:]
            break
    return res
    
    


## codecademy
def merge_co(items):
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_co(left_split)
    right_sorted = merge_co(right_split)

    return compare_co(left_sorted, right_sorted)
def compare_co(left, right):
    result = []
    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right

    return result






