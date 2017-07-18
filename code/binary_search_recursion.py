import math


def binary_search_re(data, target, start, end):
    mid = (start + end) // 2
    if target == data[mid]:
        return mid
    elif target < data[mid]:
        end = mid - 1
    elif target > data[mid]:
        start = mid + 1
    else:
        return None
    return binary_search_re(data, target, start, end)

data = [i for i in range(10000)]
target = 8200
idx = binary_search_re(data, target, 0, len(data))

if idx:
    print("log2-{} : {}".format(target, math.log(target, 2)))
    print('{}의 인덱스는 {}이다.'.format(target, idx))
else:
    print('못찾았다')
