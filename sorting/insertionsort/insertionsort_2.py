def insertionsort(A: list):
    n = len(A)
    for i in range(0, n):
        place = i
        insert = A[i]
        j = i - 1
        while True:
            if A[j] <= A[i]:
                break
            j -= 1

        for k in range(i - 1, j, -1):
            swap(A, k, k + 1)
            place = k

        A[place] = insert
        print(A)


def swap(a: list, pos1, pos2):
    buff = a[pos1]
    a[pos1] = a[pos2]
    a[pos2] = buff


if __name__ == '__main__':
    listA = [6, 5, 4, 3, 2, 1]
    insertionsort(listA)
    print(listA)
