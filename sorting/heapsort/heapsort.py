from utils import swap


def sift(A: list, l: int, r: int):
    # l: positie waar de heap-eigenschap onderzocht moet worden\
    # r: laatste positie van de heap
    i = l
    j = 0
    placefound = False
    origin = A[l]

    while ((2 * i + 1) <= r) and not placefound:
        j = 2 * i + 1  # j is nu de index van het linkerkind vanwege de eigenschap van de binaire boomstructuur: leftChild = 2*i+1
        if j < r:
            # hier weten we dat we nog binnen het bereik zijn van de heap,
            # moeten we weten want we moeten de kinderen vergelijken kunnen -> als heap size =j dan
            # weten we dat A[j] het enigste kind van origin is
            if A[j] > A[j + 1]:
                # als het linkerkind groter is dan zetten we de index naar het rechterkind --> we bouwen een min heap op
                # waar het kleinste element vanboven staat
                j = j + 1
        if origin > A[j]:
            A[i] = A[j]  # zet het kleinste op de positie
            i = j  # schuif de index naar de positie van het kind dat eerder gevonden was als kleinste kind van A[i]
        else:
            # de origin zit goed, alle kinderen zijn dus groter of gelijk aan de origin label
            placefound = True
    # zet het element wat vooraan in de boom stond op de gevonden plaats
    A[i] = origin


def heapsort(A: list):
    n = len(A)
    mid = n//2 -1

    for l in range(mid, -1, -1):
        sift(A, l, n - 1)

    for r in (n - 1, 1, -1):
        swap(A, pos1=0, pos2=r)
        sift(A, 1, r)
    A.reverse()


if __name__ == '__main__':
    arr: list = [5, 1, 9, 10, 30, 11, 3, 8]
    heapsort(arr)
    print(arr)
