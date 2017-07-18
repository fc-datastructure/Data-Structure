def linear_search(data, target):
    for idx in range(len(data)):
        if data[idx] == target:
            return idx
    return None

data = [i for i in range(10000)]
target = 7000

idx = linear_search(data, target)

if idx is None:
    print("존재하지 않습니다.")
else:
    print("찾는 데이터의 인덱스 {}이고 데이터는 {}입니다.".format(idx, data[idx]))