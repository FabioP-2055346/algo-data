def bucketsort(A: list):
    buckets: list = [0] * (max(A) + 1)
    for i in range(0, len(A)):
        index = A[i]
        buckets[index] += 1

    j: int = 0
    for k in range(0, len(buckets)):
        for m in range(0, buckets[k]):
            A[j] = k
            j = j+1


if __name__ == '__main__':
    arr = [1, 1, 1, 2, 5, 3, 2, 4]

    print("Given array: ")
    print(arr)

    bucketsort(arr)
    print()
    # print array after sorting
    print("Sorted array: ")
    print(arr)
