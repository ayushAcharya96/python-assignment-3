# Bubble Sort

def bubble_sort(input_list):
    n = len(input_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return input_list

# Driver Code
arr = [8, 9, 1, -54, 75, 34, 12, -9, 0 , 28]

print(bubble_sort(arr))
