from utils import swap


def bubble_sort(A: list):
    n = len(A)
    for i in range(0, n, +1):

        for j in range(n - 1, i, -1):
            if not A[j - 1] <= A[j]:
                swap(A, j, j - 1)


def better_bubble_sort(A: list):
    n = len(A)

    for i in range(0, n, +1):
        swaped = False
        for j in range(n - 1, i, -1):
            if not A[j - 1] <= A[j]:
                swap(A, j, j - 1)
                swaped = True
        print('Round: ' + str(i+1))
        if not swaped:
            break


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    sorterArr = [1,2,3,4,5,6,8,7]
    print("Given array is", end="\n")
    print(arr)
    better_bubble_sort(sorterArr)
    print("Sorted array is: ", end="\n")
    print(sorterArr)
