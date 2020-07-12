# Insertion Sort

def insertion_sort(input_array):
    for i in range(1, len(input_array)):
        key = input_array[i]
        index = i
        while index > 0 and key < input_array[index - 1]:
            input_array[index] = input_array[index - 1]
            index -= 1
        input_array[index] = key
    return input_array


# Driver code
arr = [8, 9, 1, -54, 75, 34, 12, -9, 0 , 28]

print(insertion_sort(arr))