import math


def binary_search(data, target):
    """
    :param data: 무조건 데이터는 정렬된 상태의 리스트로 전달해야 함
    :param target: 찾고자 하는 넘버
    :return: 없으면 None을 반환, 찾으면 데이터의 리스트 인덱스를 반환
    """

    # data.sort()
    start = 0
    end = len(data) - 1
    i = 1

    while start <= end:
        print('{}번째'.format(i))
        i += 1
        mid = (start + end) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None


data = [i for i in range(10000)]
target = 8200
idx = binary_search(data, target)

if idx:
    print("log2-{} : {}".format(target, math.log(target, 2)))
    print('{}의 인덱스는 {}이다.'.format(target, idx))
else:
    print('못찾았다')
