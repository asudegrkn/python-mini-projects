"""
 n: disk sayısı,
 source: kaynak,
 destination: hedef,
 b: tampon
"""


def hanoi(n, source, destination, b):
    assert n > 0
    if n == 1:
        print("Move", source, 'to', destination)
    else:
        hanoi(n - 1, source, b, destination)
        hanoi(1, source, destination, b)
        hanoi(n - 1, b, destination, source)


n = 4
hanoi(n, 'A', 'B','C')
