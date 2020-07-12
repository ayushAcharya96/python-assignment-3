# Binary Search

def binary_search(arr, start, end, key):
    if end >= start:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, start, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, end, key)
    else:
        return -1

# Driver code
arr = [-54, -9, 0, 1, 8, 9, 12, 28, 34, 75]
print(binary_search(arr, 0, len(arr) - 1, 8))
