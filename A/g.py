# Interpolation Search

def interpolation_search(arr, key):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high and key >= arr[low] and key <= arr[high]:
        if low == high:
            if arr[low] == key:
                return low
            return -1
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (key - arr[low])))
        if arr[pos] == key:
            return pos
        if arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Driver code
arr = [-54, -9, 0, 1, 8, 9, 12, 28, 34, 75]
print(interpolation_search(arr, 34))
