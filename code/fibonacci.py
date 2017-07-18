"""
피보나치 수열을 만드는 재귀함수
"""


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print([fibonacci(i) for i in range(10)])

"""
generator를 이용하는 방법(메모리적으로 효율이 굉장히 좋음)
"""


def fibo_gen(n):
    a = b = 1

    for i in range(n):
        yield a
        a, b = b, a + b

f = fibo_gen(10)
for i in range(10):
    print(next(f), end=' ')