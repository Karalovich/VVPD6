"""Королевич Анрей 4 лаба"""


def sequence(n: int) -> list[int]:
    main = [n]
    while n != 1:
        if not n % 2:
            n = n / 2
            main.append(int(n))
        else:
            n = n * 3 + 1
            main.append(int(n))
    return main


def maxim(n: int) -> int:
    main = sequence(n)
    max_n = 0
    for i in main:
        if i > max_n:
            max_n = i
    return max_n

