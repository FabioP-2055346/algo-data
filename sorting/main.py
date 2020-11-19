import math


def partition(a: list, left: int, right: int):
    i = left
    j = right
    index = math.floor((left + right) / 2)
    pivot = a[index]

    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            buff = a[i]
            a[i] = a[j]
            a[j] = buff
            i += 1
            j -= 1
    if left < j:
        partition(a, left, j)
    if i < right:
        partition(a, i, right)


def quicksort(a: list):
    partition(a, 0, len(a) - 1)


if __name__ == '__main__':
    reeks = [10, 8, 1, 9, 4, 7, 3, 11, 88, 6]
    quicksort(reeks)
    print(reeks)
