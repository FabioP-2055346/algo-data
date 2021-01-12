def insertionsort(A: list):
    n = len(A)
    for i in range(1, n, +1):
        origin = A[i]
        place = i

        while True:
            placefound = A[place - 1] <= origin

            if not placefound:
                bigger_than_current_value = A[place - 1]
                A[place] = bigger_than_current_value
                place = place - 1  # zak verder naar links

            if placefound or place == 0:
                break

        A[place] = origin


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    print(arr)
    insertionsort(arr)
    print("Sorted array is: ", end="\n")
    print(arr)
