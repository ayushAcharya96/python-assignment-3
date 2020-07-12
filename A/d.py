# Merge Sort


def merge(L, R, A):
    nL = len(L)
    nR = len(R)
    i = j = k = 0
    while i < nL and j < nR:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        arr = merge(left, right, arr)

# Driver code
arr = [8, 9, 1, -54, 75, 34, 12, -9, 0 , 28]

merge_sort(arr)
print(arr)

