# Linear Search

def linear_search(arr, key):
    for i, value in enumerate(arr):
        if value == key:
            return i
    return -1

# Driver code
arr = [8, 9, 1, -54, 75, 34, 12, -9, 0 , 28]

print(linear_search(arr, -1))