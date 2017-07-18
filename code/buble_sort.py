def buble_sort(data):
    for i in range((len(data)-1), 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                print(data)


data = [7, 8, 2, 4, 6, 15, 22, 11, 9]

buble_sort(data)