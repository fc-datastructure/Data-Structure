def hanoi(num, _from, _by, _to):
    if num == 1:
        print("{}에서 {}로 {}번째 원반 이동".format(_from, _to, num))
        return

    hanoi(num-1, _from, _to, _by)
    print("{}에서 {}로 {}번째 원반 이동".format(_from, _to, num))
    hanoi(num-1, _by, _from, _to)


hanoi(3, 'A', 'B', 'C')