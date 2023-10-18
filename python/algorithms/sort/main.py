from bubble import bubble, bubble_opt
from merge import merge_r, merge_m, merge_co, merge_m_r
from quick import quick, quick_p, quick_r
import numpy as np
import random

def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

# random arr

arr = random_int_list(1,10,10)

# random arr without duplicates

# arr = list(range(20, 0, -1))
# np.random.shuffle(arr)


print(arr)

arr = [1]
# bubble
# res = bubble(arr)
# res = bubble_opt(arr)

# merge
# res = merge_m(arr)
# res = merge_m_r(arr)
# res = merge_r(arr)
# res = merge_co(arr)

# quick
# res = quick(arr)
# res = quick_p(arr)
res = quick_r(arr)


print(res)


